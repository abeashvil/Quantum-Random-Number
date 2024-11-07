from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_aer import AerSimulator
import os
from dotenv import load_dotenv, dotenv_values
 
from qiskit_ibm_runtime import QiskitRuntimeService
load_dotenv()

# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token=os.getenv('MY_KEY'),
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



