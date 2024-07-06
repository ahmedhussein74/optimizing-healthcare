# Calculate Constraint Violations
import numpy as np


def compute_violations(x, y, z, o, v, Drt, D_t, Hi, Si, Mipkt, Oi, Wit, B, Fij):
    N, T = x.shape
    P, T = y.shape
    R, T = z.shape

    violations = []

    # Staff Availability Constraint (Equality)
    staff_availability_violation = np.abs(np.sum(x, axis=0) - D_t)
    violations.append(staff_availability_violation)

    # Maximum Working Hours Constraint (Inequality)
    working_hours_violation = np.maximum(0, np.sum(x, axis=1) - Hi)
    violations.append(working_hours_violation)

    # Patient Scheduling Constraint (Equality)
    patient_scheduling_violation = np.abs(np.sum(y, axis=1) - 1)
    violations.append(patient_scheduling_violation)

    # Resource Allocation Constraint (Equality)
    resource_allocation_violation = np.abs(np.sum(z, axis=1) - 1)
    violations.append(resource_allocation_violation)

    # Skill Level Constraint (Inequality)
    skill_level_violation = np.maximum(0, Mipkt - np.sum(x * Si[:, np.newaxis]))
    violations.append(skill_level_violation)

    # Overtime Constraint (Inequality)
    overtime_violation = np.maximum(0, np.sum(x, axis=1) - Hi - Oi)
    violations.append(overtime_violation)

    # Budget Constraint (Inequality)
    staff_cost = np.sum(Wit * x) + np.sum(Oi * o)
    resource_cost = np.sum(Drt * z)
    total_cost = staff_cost + resource_cost
    budget_violation = np.maximum(0, total_cost - B)
    violations.append(budget_violation)

    # Workload Balance Constraint (Inequality)
    total_working_hours = np.sum(x, axis=1)
    # Create a mask for pairs of indices
    i_indices, j_indices = np.triu_indices(N, k=1)
    working_hours_diff = np.abs(
        total_working_hours[i_indices] - total_working_hours[j_indices]
    )
    F_upper_triangular = Fij[i_indices, j_indices]
    workload_balance_violation = np.maximum(0, working_hours_diff - F_upper_triangular)
    violations.append(workload_balance_violation)

    return violations
