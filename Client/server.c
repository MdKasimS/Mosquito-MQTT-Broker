#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#include <winsock2.h>
#pragma comment(lib, "ws2_32.lib")
#else
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#endif

#define PORT 12345
#define BUFFER_SIZE 1024

int main() {
    // Initialize socket library (Windows)
#ifdef _WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        perror("Failed to initialize Winsock");
        return 1;
    }
#endif

    // Create socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Socket creation failed");
        return 1;
    }

    // Bind socket
    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Socket binding failed");
        return 1;
    }

    // Listen for connections
    if (listen(server_socket, 5) == -1) {
        perror("Listen failed");
        return 1;
    }

    printf("Server listening on port %d\n", PORT);

    // Accept connections and handle clients
    while (1) {
        struct sockaddr_in client_addr;
        socklen_t client_addr_size = sizeof(client_addr);

        int client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_size);
        if (client_socket == -1) {
            perror("Accept failed");
            continue;
        }

        printf("Client connected\n");

        // Receive and send data to client
        char buffer[BUFFER_SIZE];
        while (1) {
            memset(buffer, 0, BUFFER_SIZE);

            int bytes_received = recv(client_socket, buffer, BUFFER_SIZE, 0);
            if (bytes_received <= 0) {
                printf("Client disconnected\n");
                break;
            }

            printf("Received: %s", buffer);

            // Echo the message back to the client
            send(client_socket, buffer, bytes_received, 0);
        }

#ifdef _WIN32
        closesocket(client_socket);
#else
        close(client_socket);
#endif
    }

    // Clean up
#ifdef _WIN32
    WSACleanup();
#endif

    return 0;
}
