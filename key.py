from qiskit import QuantumCircuit, Aer, execute
from numpy.random import randint
def bb84_key(length):
    alice_bits = randint(2, size=length)
    alice_bases = randint(2, size=length)
    
    bob_bases = randint(2, size=length)
    
    alice_circuits = []
    for i in range(length):
        qc = QuantumCircuit(1,1)
        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 1:
            qc.h(0)
        alice_circuits.append(qc)
    
    backend = Aer.get_backend('statevector_simulator')
    alice_results = []
    for qc in alice_circuits:
        result = execute(qc, backend).result()
        alice_results.append(result.get_statevector())
    
    bob_results = []
    for i in range(length):
        qc = QuantumCircuit(1,1)
        if bob_bases[i] == 1:
            qc.h(0)
        result = execute(qc, backend).result()
        bob_results.append(result.get_statevector())
    
    key = []
    for i in range(length):
        if alice_bases[i] == bob_bases[i]:
            if alice_bases[i] == 0:
                key.append(alice_bits[i])
            else:
                bob_measure = 0 if bob_results[i][0] > 0 else 1
                key.append(bob_measure)
    return key