import numpy as np
import itertools

def dagg (A):
    """Computes the dagger of a matrix"""
    return A.T.conj()

def list_to_index_alpha_beta (alpha,beta):
    """returns the index corresponding to entries alpha and beta defined as list"""
    n = len(alpha)
    max_val = 4**n
    if len(beta) != n:
        raise("alpha and beta have mismatching dimensions.")
    ind_a = 0
    ind_b = 0
    for i in range(n):
        ind_a += 4**(n-i-1)*alpha[i]
        ind_b += 4**(n-i-1)*beta[i]
    return ind_a*max_val + ind_b

def index_to_lst_alpha_beta (index,n):
    """returns the entries alpha and beta defined as list to the corresponding index"""
    ind_a, ind_b = divmod(index,4**n)
    alpha = to_basis(ind_a,4)
    beta = to_basis(ind_b,4)
    if len(alpha) < n:
        for _ in range(n-len(alpha)):
            alpha.insert(0,0)
    if len(beta) < n:
        for _ in range(n-len(beta)):
            beta.insert(0,0)
    return alpha, beta

def list_to_index_r_s (r,s):
    """returns the index corresponding to entries r and s defined as list"""
    n = len(r)
    max_val = 6**n
    if len(s) != n:
        raise("r and s have mismatching dimensions.")
    ind_a = 0
    ind_b = 0
    for i in range(n):
        ind_a += 6**(n-i-1)*r[i]
        ind_b += 6**(n-i-1)*s[i]
    return ind_a*max_val + ind_b

def index_to_lst_r_s (index,n):
    """returns the entries alpha and beta defined as list to the corresponding index"""
    ind_r, ind_s = divmod(index,6**n)
    r = to_basis(ind_r,6)
    s = to_basis(ind_s,6)
    if len(r) < n:
        for _ in range(n-len(r)):
            r.insert(0,0)
    if len(s) < n:
        for _ in range(n-len(s)):
            s.insert(0,0)
    return r, s

def sigma (index): 
    """Single qubit Pauli matrices as a list

    Args:
        index (int): index of the Pauli matrix

    Returns:
        ndarray: Pauli matrix of the respective index
    """
    s = [np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
    return s[index]

def to_basis (n,b):
    """Returns n written in basis b"""
    if n == 0:
        return [0]
    digits = []
    while n> 0:
        digits.append(n%b)
        n //= b
    return digits[::-1]

def to_decimal (lst,b):
    """Returns the decimal number from a list of digit s in basis b"""
    s = len(lst)
    d = 0
    for i in range(s):
        d += b**(s-i-1)*lst[i]
    return d

def swap_digits (n,b,new_order):
    """Given a number decimal n it returns the decimal number corresponding to n, written in the basis b but digits in the new order"""
    bas = to_basis(n,b)
    app = [0 for _ in range(len(new_order)-len(bas))]
    bas_app = app + bas
    new = np.zeros(len(new_order),dtype = 'int')
    for i in range(len(new_order)):
        new[i] = bas_app[new_order[i]]
    return to_decimal(new,b)

def gen_swap (b,new_order):
    """Generates the matrix that, if multiplied to another matrix, swaps subspaces of dimension b and puts in them in the new order"""
    dim = b**len(new_order)
    S = np.zeros((dim,dim))
    for i in range(dim):
        S[i,swap_digits(i,b,new_order)] = 1
    return S

def B_left ():
    """Matrix of change of basis from computational to Pauli eigenstates"""
    B = np.array([  [0, 1,          1,          0],
                    [0, 0,          0,          0],
                    [0, 1j,         -1j,        0],
                    [0, 0,          0,          0],
                    [1, (-1-1j)/2,  (-1+1j)/2,  0],
                    [0, (-1-1j)/2,  (-1+1j)/2,  1]], dtype = 'complex')
    return B

def B_right ():
    """Matrix of change of basis from Pauli eigenstates to computational"""
    B = np.array([  [0.5, 0.5,  0.5,    0.5,    1,  0],
                    [0.5, -0.5, -0.5j,  0.5j,   0,  0],
                    [0.5, -0.5, 0.5j,   -0.5j,  0,  0],
                    [0.5, 0.5,  0.5,    0.5,    0,  1]], dtype = 'complex')
    return B

def U_1q_pauli_basis (M):
    """Transforms a single qubit unitary in the computational basis into a unitary on the basis (+,-,+i,-i,0,1)"""
    Bl = B_left()
    Br = B_right()
    M2 = np.kron(M,M.conj())
    return Bl@M2@Br

def U_2q_pauli_basis (M):
    """Transforms a two qubit unitary in the computational basis into a unitary on the basis (+,-,+i,-i,0,1) tensor itself"""
    S = gen_swap(2,[0,2,1,3])
    B_l = B_left()
    B_r = B_right()    
    B_l2 = np.kron(B_l,B_l)
    B_r2 = np.kron(B_r,B_r)
    M2 = np.kron(M,(M).conj())
    m = B_l2@S@M2@S@B_r2
    return m

def U_2q_pauli_basis_id (M):
    """Given a unitary returns the unitary written in the Pauli basis tensor identity, 
        with the subspaces in the same order as the two qubit functions G and F"""
    m = U_2q_pauli_basis(M)
    S6 = gen_swap(6,(0,2,1,3))
    m_id = S6@np.kron(m,np.eye(36))@S6    
    return m_id

def chi_from_U_1q (U):
    """Computes the chi matrix of a process associated with a unitary evolution on one qubit"""
    p = [np.trace((U@sigma(i)))/2 for i in range(4)]
    chi = np.zeros((4,4),dtype = 'complex128')
    for i in itertools.product(range(4),repeat = 2):
        chi[i] = p[i[0]]*np.conj(p[i[1]])
    return chi

def chi_from_U_2q (U):
    """Computes the chi matrix of a process associated with a unitary evolution on two qubits"""
    p = [np.trace((U@np.kron(sigma(i),sigma(j))))/4 for i in range(4) for j in range(4)]
    chi = np.zeros((16,16),dtype = 'complex128')
    for i in itertools.product(range(16),repeat = 2):
        chi[i] = p[i[0]]*np.conj(p[i[1]])
    return chi

def chi_from_U (M):
    """Computes the chi matrix of a process associated with a unitary evolution on one or two qubits"""
    if np.allclose(np.shape(M),2):
        chi = chi_from_U_1q (M)    
    if np.allclose(np.shape(M),4):
        chi = chi_from_U_2q (M)
    if np.allclose(np.shape(M),2) == False and np.allclose(np.shape(M),4) == False:
        raise("Please insert a one qubit or two qubit unitary")
    return chi