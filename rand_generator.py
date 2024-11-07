from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_aer import AerSimulator
# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="7ea9d4e3f8ead1f98c1e788b3d674352b3ab584c2604f3d915aa2b1fcb0b33285e72d03f53cb1907beedde852216642dbbc46186350d04c94f6110f740dfea6b",
    set_as_default=True,
    # Use `overwrite=True` if you're updating your token.
    overwrite=True,
)
 
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



