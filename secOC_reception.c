/*
PduR and RXIndication: The PDU Router (PduR) is responsible for routing Protocol Data
Units (PDUs) between different communication modules. 
When a PDU is received, the RXIndication function is called to indicate the reception of the PDU.
SecOC->CopyData(): The Secure Onboard Communication (SecOC) module is responsible for ensuring
the authenticity and integrity of the PDUs. The CopyData() function is used to copy the 
received data for further processing.

Freshness Value from Security Extension: The freshness value is used to protect against replay attacks. 
It is a unique value that changes with each transmission. The SecOC module retrieves this value from
the security extension.

Calculate CMAC using CSM Module: The Cryptographic Service Manager (CSM) module is used to calculate 
the Cipher-based Message Authentication Code (CMAC). The CMAC is a cryptographic checksum that
ensures the integrity and authenticity of the message. The inputs for this calculation include 
the PDU, the freshness value, and a secret key.

Compare CMAC using SecOC Module: The SecOC module compares the calculated CMAC with the CMAC 
received in the PDU. If they match, it means the message is authentic and has not been tampered with.

Verification and Tx Request to PduR: If the verification is successful, the SecOC module 
sends a transmission request to the PduR to forward the PDU to its intended destination.

This process ensures that the communication between Electronic Control Units (ECUs) 
within the vehicle is secure and protected from cyber-attacks
Refer: https://www.autosar.org/fileadmin/standards/R20-11/FO/AUTOSAR_PRS_SecOcProtocol.pdf
*/


#include <stdio.h>
#include <string.h>
#include <openssl/hmac.h>
#include <openssl/rand.h>

#define PDU_SIZE 16
#define FRESHNESS_SIZE 16
#define CMAC_SIZE 32
#define KEY_SIZE 16

// Sample data for demonstration
unsigned char pdu_data[PDU_SIZE] = "Sample PDU Data";
unsigned char received_cmac[CMAC_SIZE] = "Received CMAC";
unsigned char secret_key[KEY_SIZE] = "SecretKey";

// Function to simulate RXIndication
void RXIndication(unsigned char *pdu) {
    printf("RXIndication: PDU received.\n");
}

// Function to simulate SecOC->CopyData()
void CopyData(unsigned char *pdu) {
    printf("SecOC->CopyData: Data copied for processing.\n");
}

// Function to retrieve Freshness Value from Security Extension
void get_freshness_value(unsigned char *freshness_value) {
    RAND_bytes(freshness_value, FRESHNESS_SIZE);
    printf("Freshness Value: ");
    for (int i = 0; i < FRESHNESS_SIZE; i++) {
        printf("%02x", freshness_value[i]);
    }
    printf("\n");
}

// Function to calculate CMAC using CSM Module
void calculate_cmac(unsigned char *data, unsigned char *freshness_value, unsigned char *key, unsigned char *cmac) {
    unsigned char combined_data[PDU_SIZE + FRESHNESS_SIZE];
    memcpy(combined_data, data, PDU_SIZE);
    memcpy(combined_data + PDU_SIZE, freshness_value, FRESHNESS_SIZE);

    unsigned int len = CMAC_SIZE;
    HMAC(EVP_sha256(), key, KEY_SIZE, combined_data, sizeof(combined_data), cmac, &len);

    printf("Calculated CMAC: ");
    for (int i = 0; i < CMAC_SIZE; i++) {
        printf("%02x", cmac[i]);
    }
    printf("\n");
}

// Function to compare CMAC using SecOC module
int compare_cmac(unsigned char *calculated_cmac, unsigned char *received_cmac) {
    if (memcmp(calculated_cmac, received_cmac, CMAC_SIZE) == 0) {
        printf("CMAC verification successful.\n");
        return 1;
    } else {
        printf("CMAC verification failed.\n");
        return 0;
    }
}

// Function to simulate Tx request to PduR
void tx_request(unsigned char *pdu) {
    printf("Tx request to PduR: PDU forwarded to destination.\n");
}

// Main process
int main() {
    unsigned char freshness_value[FRESHNESS_SIZE];
    unsigned char calculated_cmac[CMAC_SIZE];

    RXIndication(pdu_data);
    CopyData(pdu_data);
    get_freshness_value(freshness_value);
    calculate_cmac(pdu_data, freshness_value, secret_key, calculated_cmac);

    if (compare_cmac(calculated_cmac, received_cmac)) {
        tx_request(pdu_data);
    } else {
        printf("Transmission request denied due to CMAC verification failure.\n");
    }

    return 0;
}
