# Simple Blockchain Application
This is a simple blockchain application implemented in Python. It allows you to create a blockchain network and add blocks to the chain. The application uses Docker for containerization and Kubernetes for deployment and management of the blockchain nodes.

### Prerequisites
Before running the blockchain application, make sure you have the following dependencies installed:

**Docker:** [Install Docker](https://docs.docker.com/get-docker/)

**Kubernetes:** [Install Kubernetes](https://kubernetes.io/docs/setup/)

### Dockerization
To containerize the blockchain application using Docker, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Build the Docker image by running the following command:
`docker build -t blockchain-app:latest .`
4. Once the image is built, you can verify it by running:
`docker images`

### Kubernetes Deployment
To deploy the blockchain application using Kubernetes, follow these steps:

1. Make sure you have a Kubernetes cluster set up and configured.
2. Modify the `deployment.yaml` file:
   - Replace `<your-docker-registry>` with the appropriate Docker registry where you intend to push your Docker image. 
3. Apply the Kubernetes Deployment by running the following command:
`kubectl apply -f deployment.yaml`
4. Verify that the deployment is successful by checking the created pods:
`kubectl get pods`
5. Modify the `service.yaml` file if necessary (e.g., change the `port` or `targetPort`).
6. Apply the Kubernetes Service by running the following command:
`kubectl apply -f service.yaml`
7. Verify that the service is created and the application is accessible:
`kubectl get services`

### Interacting with the Blockchain Application
Once the blockchain application is deployed, you can interact with it using the exposed API.

Here's an example using cURL:

- To add a block to the blockchain:

`curl -X POST http://<service-ip>:<service-port>/blocks -d '{"data":"Block Data"}'`

- To retrieve the entire blockchain:

`curl http://<service-ip>:<service-port>/blocks`

Note: Replace `<service-ip>` and `<service-port>` with the appropriate IP and port values of the Kubernetes service.

### Cleanup
To clean up and remove the deployed blockchain application, run the following commands:

`kubectl delete deployment blockchain-app-deployment`

`kubectl delete service blockchain-app-service`

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### License
This project is licensed under the [Apache License - 2.0](https://www.apache.org/licenses/LICENSE-2.0).