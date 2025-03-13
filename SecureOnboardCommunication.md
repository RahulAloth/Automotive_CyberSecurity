Refer: https://cdn.vector.com/cms/content/events/2018/Webinars18/Vector_Webinar_ACS_20180614.pdf
# Secure Onboard Communication (SecOC)

SecOC is a security protocol integrated into the AUTOSAR architecture to ensure the authenticity and 
integrity of messages exchanged between Electronic Control Units (ECUs) within a vehicle. It provides robust security measures to protect in-vehicle communication from cyber threats.

## SecOC Message Transmission

The process of SecOC message transmission involves several steps to ensure secure communication:

### 1. PDU Reception and Transmission

- **PDU Reception**: Protocol Data Units (PDUs) are received by the PDU Router (PDU R). The PDU R is responsible for routing PDUs to the appropriate modules within the vehicle's network.
- **SecOC Processing**: Once the PDU is received by the PDU R, it is sent to the SecOC module. The SecOC module checks the authenticity and integrity of the received message.

### 2. SecOC Module Components

SecOC relies on several components to perform its security functions:

- **CSM-CryIF Interface**: The Crypto Service Manager (CSM) and Crypto Interface (CryIF) provide cryptographic services to the SecOC module. These interfaces handle encryption, decryption, and key management operations.
- **Freshness Value Manager (FVM)**: The FVM ensures that each message has a unique freshness value, preventing replay attacks. It manages the freshness values for each secured communication link.
- **Key Manager**: The Key Manager handles the distribution and management of cryptographic keys used by the SecOC module.

### 3. Message Verification

- **Integrity Check**: The SecOC module verifies the integrity of the received message by checking the cryptographic authentication information added to the PDU.
- **Authenticity Check**: The SecOC module ensures that the message comes from a trusted source by verifying the cryptographic signature.

### 4. Message Unpacking and Application

- **COM Module**: After the SecOC module verifies the message, the Communication (COM) module unpacks the message and sends it to the appropriate application within the vehicle's network.
- **Application Processing**: The application processes the received message and performs the necessary actions based on the data.

By implementing these steps, SecOC ensures that in-vehicle communication is secure, protecting against unauthorized access and tampering.

## Freshness Value Manager (FVM)

The Freshness Value Manager is a crucial component in the SecOC module, responsible for ensuring the uniqueness and timeliness of messages to prevent replay attacks. Here's how it works:

### 1. Freshness Values

- **Purpose**: Freshness values are unique identifiers added to each message to ensure that it is new and not a replay of an old message.
- **Generation**: The FVM generates freshness values for each secured communication link. These values can be based on counters, timestamps, or other mechanisms.
- **Management**: The FVM keeps track of the freshness values used in communication, ensuring that each message has a unique value.

### 2. Integration with SecOC

- **Sender Side**: On the sender side, the SecOC module retrieves the freshness value from the FVM and adds it to the outgoing message.
- **Receiver Side**: On the receiver side, the SecOC module checks the freshness value of the incoming message to ensure it is valid and not a replay.

## Key Manager

The Key Manager is responsible for handling cryptographic keys used in the SecOC module. It ensures that keys are securely managed and distributed. Here's how it works:

### 1. Key Management

- **Key Generation**: The Key Manager generates cryptographic keys used for securing communication.
- **Key Distribution**: It securely distributes keys to the relevant modules and ECUs within the vehicle.
- **Key Storage**: Keys are stored securely, often within Hardware Security Modules (HSMs) to protect them from unauthorized access.

### 2. Integration with SecOC

- **Key Retrieval**: The SecOC module retrieves cryptographic keys from the Key Manager to perform encryption and decryption operations.
- **Key Rotation**: The Key Manager handles key rotation and updates to ensure that keys are regularly refreshed and remain secure.

## Message Transmission Process

Here's a detailed overview of the message transmission process involving the FVM and Key Manager:

### 1. PDU Reception and Transmission

- **PDU Reception**: Protocol Data Units (PDUs) are received by the PDU Router (PDU R) and sent to the SecOC module.
- **SecOC Processing**: The SecOC module retrieves the freshness value from the FVM and the cryptographic key from the Key Manager. It then adds authentication information to the PDU.

### 2. Message Verification

- **Integrity Check**: The SecOC module verifies the integrity of the received message by checking the cryptographic authentication information.
- **Authenticity Check**: The SecOC module ensures that the message comes from a trusted source by verifying the cryptographic signature.

### 3. Message Unpacking and Application

- **COM Module**: After verification, the COM module unpacks the message and sends it to the appropriate application within the vehicle's network.
- **Application Processing**: The application processes the received message and performs the necessary actions based on the data.

By implementing the Freshness Value Manager and Key Manager modules, the SecOC framework ensures secure and reliable communication within the vehicle, protecting against replay attacks and unauthorized access.
