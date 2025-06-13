import scipy
from .utils import *

def f_alpha_beta():
    """tr[r sigma_alpha s sigma_beta] with r and s in the basis (+,-,+i,-i,0,1) and sigma_a,sigma_b = Id,X,Y,Z"""
    f_ab = np.array(np.array([[1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j ],[ 1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,-1. +0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j],[ 0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0. +0.j,-1. +0.j,  -0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j],[ 0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j,   0.5+0.j,  -0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0. +0.j,-1. +0.j],[ 1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,-1. +0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j],[ 1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j],[ 0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j,  -0.5+0.j,   0.5+0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j, -0.5+0.j,   0.5+0.j,   0. +0.j,0. +0.j,   0. -0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,0. +0.j,   0. +1.j,   0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -1.j,0. +0.j, ],[ 0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. +0.5j,  0. -0.5j, -0.5+0.j,   0.5+0.j,   0. -0.5j,  0. -0.5j,0. +0.j,   0. -1.j,   0. -0.5j,  0. -0.5j,  0. +0.5j,  0. +0.5j,  0. +1.j,0. +0.j,   0. +0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,0. +0.j,   0. +0.j,  -0.5+0.j,   0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j],[ 0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0. +0.j,-1. +0.j,  -0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j], [ 0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j,  -0.5+0.j,   0.5+0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j, -0.5+0.j,   0.5+0.j,   0. +0.j,0. +0.j,   0. +0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,0. +0.j,   0. -1.j,   0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +1.j,0. +0.j],[ 0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j],[ 0. +0.j,   0. +1.j,   0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. -1.j,0. +0.j,   0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. +0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j,  -0.5+0.j,   0.5+0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j, -0.5+0.j,   0.5+0.j,   0. +0.j,0. +0.j ],[ 0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j,   0.5+0.j,  -0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,  -0.5+0.j,   0. +0.j,-1. +0.j ],[ 0. +0.j,   0. +0.j,   0. -0.5j,  0. +0.5j,  0.5+0.j,  -0.5+0.j,   0. +0.j,0. +0.j,   0. -0.5j,  0. +0.5j, -0.5+0.j,   0.5+0.j,   0. +0.5j,  0. +0.5j,0. +0.j,   0. +1.j,   0. +0.5j,  0. +0.5j,  0. -0.5j,  0. -0.5j,  0. -1.j,0. +0.j,   0. -0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,   0. -0.5j,  0. +0.5j,0. +0.j,   0. +0.j,  -0.5+0.j,   0.5+0.j,   0. -0.5j,  0. +0.5j,  0. +0.j,0. +0.j ],[ 0. +0.j,   0. -1.j,   0. -0.5j,  0. -0.5j,  0. -0.5j,  0. -0.5j,  0. +1.j,0. +0.j,   0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. +0.5j,  0. -0.5j,0. +0.j,   0. +0.j,   0.5+0.j,  -0.5+0.j,   0. +0.5j,  0. -0.5j,  0. +0.j,0. +0.j,  -0.5+0.j,   0.5+0.j,   0. +0.5j,  0. -0.5j,  0.5+0.j,  -0.5+0.j,0. +0.j,   0. +0.j,   0. +0.5j,  0. -0.5j, -0.5+0.j,   0.5+0.j,   0. +0.j,0. +0.j ],[ 0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,0. +0.j,   1. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   1. +0.j,0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,1. +0.j,   0. +0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0.5+0.j,   0. +0.j,1. +0.j ]]).T,dtype = 'complex128')
    return f_ab/18

def g_alpha_beta ():
    """Function that given r and s in the basis (+,-,+i,-i,0,1) and returns g_alpha_beta with sigma_a,sigma_b = Id,X,Y,Z"""
    f_ab = f_alpha_beta()
    return np.linalg.pinv(f_ab)

def g_entry_optimal_1q (U, gd):
    """Computes the optimized entry gd with respect to the evolution defined by U (single qubit)"""
    f_ab = f_alpha_beta()
    g_ab = g_alpha_beta()
    chi = chi_from_U(U)
    U_pauli = dagg(np.kron(U_1q_pauli_basis(U),np.eye(6)))  # U in the Pauli basis and correct subspaces order
    p_vec = f_ab@chi.flatten()  # probability vector
    g_U = g_ab[gd]@U_pauli  # rotated g

    K = scipy.linalg.null_space(f_ab.T).T # kernel of f
    M = np.multiply(K,p_vec)@dagg(K)
    M_inv = np.linalg.inv(M)
    gf = np.multiply(g_U.conj(),p_vec)
    v = K@gf
    x_opt = -(M_inv@v).conj() # optimized parameters
    g_U_opt = g_ab[gd]@U_pauli + x_opt @ K  # optimized g
    val_opt = np.abs(g_U_opt)**2@p_vec  # minimum value
    return g_U_opt, val_opt

def g_entry_optimal_2q (U,gd):
    """Computes the optimized entry gd with respect to the evolution defined by U (two qubits)"""
    f_ab = f_alpha_beta()
    F_ab = np.kron(f_ab,f_ab)
    g_ab = g_alpha_beta()
    G_ab = np.kron(g_ab,g_ab)
    S4 = gen_swap(4,[0,2,1,3])
    chi = chi_from_U(U)
    U_pauli = dagg(U_2q_pauli_basis_id(U))  # U in the Pauli basis and correct subspaces order
    p_vec = F_ab@S4@chi.flatten()   # probability vector
    G_u = G_ab[gd]@U_pauli  # rotated g

    K = scipy.linalg.null_space(F_ab.T) # kernel of f
    v = np.multiply(G_u,np.sqrt(p_vec))
    M = np.multiply(K.T,np.sqrt(p_vec)).T
    A = dagg(M)@M
    b = dagg(M)@v
    x_opt = -np.linalg.pinv(A) @ b  # optimized parameters
    g_U_opt = G_u + K@x_opt # optimized g
    val_opt = np.abs(g_U_opt)**2@p_vec  # minimum value
    return g_U_opt, val_opt

def g_entry_optimal (Un,gd):
    """Computes the optimized entry gd with respect to the evolution defined by U (one or two qubits)"""
    if np.allclose(np.shape(Un),2):
        g_U_opt, val_opt = g_entry_optimal_1q (Un,gd)  
    if np.allclose(np.shape(Un),4):
        g_U_opt, val_opt = g_entry_optimal_2q (Un,gd)
    if np.allclose(np.shape(Un),2) == False and np.allclose(np.shape(Un),4) == False:
        raise("Please insert a one qubit or two qubit unitary")
    return g_U_opt, val_opt

def g_optimal (Un):
    """Computes the optimized function with respect to the evolution defined by U (one or two qubits)"""
    if np.allclose(np.shape(Un),2):
        g_op_lst = []
        for gd in range(16):
            g_U_opt, val_opt = g_entry_optimal_1q (Un,gd)  
            g_op_lst.append(g_U_opt)
        g_op_tot = np.vstack(g_op_lst)
    if np.allclose(np.shape(Un),4):
        g_op_lst = []
        for gd in range(16**2):
            g_U_opt, val_opt = g_entry_optimal_2q (Un,gd)  
            g_op_lst.append(g_U_opt)
        g_op_tot = np.vstack(g_op_lst)
    if np.allclose(np.shape(Un),2) == False and np.allclose(np.shape(Un),4) == False:
        raise("Please insert a one qubit or two qubit unitary")
    return g_op_tot
