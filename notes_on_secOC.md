# Automotive Cybersecurity and SecOC

**SecOC (Secure Onboard Communication)** is a module in AUTOSAR (AUTomotive Open System ARchitecture) designed to ensure secure communication within automotive systems. It protects against unauthorized manipulation and replay attacks.

## Key Concepts

### Authentic I-PDU

- **Definition**: An AUTOSAR I-PDU (Protocol Data Unit) that requires protection against unauthorized manipulation and replay attacks.
- **Purpose**: Ensures the integrity and authenticity of the data being transmitted.

### Secured I-PDU

- **Definition**: An AUTOSAR I-PDU protected with SecOC.
- **Components**:
  - **Authentic I-PDU**: The original data that needs protection.
  - **Authenticator (e.g., MAC - Message Authentication Code)**: A code used to verify the authenticity of the data.
  - **Freshness Value (Optional)**: A value used to prevent replay attacks by ensuring that each message is unique.

## Structure of Secured I-PDU

A Secured I-PDU consists of:

- **Authentic I-PDU**: The core data that needs protection.
- **Freshness Value (Optional)**: Used to create the Authenticator and ensure the message is unique.
- **Authenticator (e.g., MAC)**: Ensures the data's integrity and authenticity.

## Variability

The length of the Authentic I-PDU, Freshness Value, and Authenticator within a Secured I-PDU can vary depending on the specific requirements of each uniquely identifiable Secured I-PDU.

## Example

Imagine a scenario where a vehicle's control unit sends a command to another unit. The command (Authentic I-PDU) is protected by adding a Freshness Value and an Authenticator. This ensures that the command is not tampered with and is unique, preventing replay attacks.

## Summary

SecOC in AUTOSAR provides a robust framework for securing communication within automotive systems by protecting data against unauthorized manipulation and replay attacks. The use of Authentic I-PDUs, Secured I-PDUs, Freshness Values, and Authenticators ensures the integrity and authenticity of the transmitted data.
