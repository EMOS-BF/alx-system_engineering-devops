=>Description

3 firewalls: The firewalls will be used to secure the network and protect the servers from unauthorized access. They will be configured to allow only necessary traffic to pass through and block all other traffic.

SSL certificate: We will install an SSL certificate on the web server to serve traffic over HTTPS. This will encrypt the traffic between the user's browser and the web server, ensuring that sensitive information such as passwords and credit card details are protected.

3 monitoring clients: We will install monitoring agents on each server to collect performance metrics and logs. The data will be sent to a centralized monitoring service such as SumoLogic. This will help us to identify and troubleshoot issues quickly and proactively.

=>Explanation of specific components:

Firewalls: Firewalls are essential to secure the network and protect the servers from unauthorized access. They are the first line of defense in any security infrastructure. The firewalls will be configured to allow only necessary traffic to pass through and block all other traffic.

SSL certificate: Serving traffic over HTTPS ensures that the traffic is encrypted and secure. This is especially important when sensitive information is being transmitted, such as credit card details or login credentials.

Monitoring: Monitoring is important to ensure that the web infrastructure is performing optimally and there are no issues that could lead to downtime. By installing monitoring agents on each server, we can collect performance metrics and logs, which can be analyzed to identify any issues or potential issues. The data collected by the monitoring agents will be sent to a centralized monitoring service such as SumoLogic, where it can be analyzed and acted upon.

Monitoring QPS: To monitor web server QPS, we can use tools such as Prometheus or Grafana, which provide real-time visibility into the performance of the web server. We can monitor metrics such as requests per second, response time, and error rate to ensure that the web server is performing optimally.

=>Issues with the infrastructure:

Terminating SSL at the load balancer level: This is an issue because it adds extra latency to the SSL handshake process and increases the load on the load balancer. To mitigate this, we can use SSL offloading, which involves terminating SSL at the web server level.

One MySQL server capable of accepting writes: This is an issue because it creates a single point of failure. To mitigate this, we can implement a MySQL primary-replica cluster with multiple replicas that can accept writes. This will ensure that if one server fails, another server can take over without causing downtime.

Servers with all the same components: This might be a problem because it creates a single point of failure. If a component such as the web server fails, it will affect all servers in the infrastructure. To mitigate this, we can implement redundancy by adding additional servers with different components to the infrastructure. This will ensure that if one component fails, another can take over without causing downtime.