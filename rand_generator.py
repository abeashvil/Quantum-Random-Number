from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_aer import AerSimulator

 
# Load saved credentials
service = QiskitRuntimeService()


def generate_rand():
    #creating a quantum circuit containing the qubits and classical bits.
    qubit = QuantumRegister(16, "Q")
    classical = ClassicalRegister(16, "C")
    circuit = QuantumCircuit(qubit, classical)
    #applying the hadamard gate to all qubits in order to put them in a superposition state
    circuit.h(range(16))
    #measuring all the qubits, and storing the results within the classical bits we made
    circuit.measure(qubit, classical) 

    #running the simulator and getting the results
    result = AerSimulator().run(circuit, shots=1).result()
    counts = result.get_counts()

    print(counts)

    binary = ""
    for key in counts:
        binary = key

    return (int(binary, 2))



