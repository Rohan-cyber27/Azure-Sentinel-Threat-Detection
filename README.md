# Azure-Sentinel-Threat-Detection

![Screenshot 2024-08-17 174654](https://github.com/user-attachments/assets/b6f9dda9-7995-443e-9c8a-2a0792b52243)


In this project, I focused on creating a cybersecurity monitoring environment in Azure, designed to detect and analyze potential security threats in real-time. The project involved setting up Windows and Linux Virtual Machines (VMs) within the same Virtual Network (VNet) and Resource Group, configuring them to attract potential attacks, and using Azure Sentinel for monitoring and visualization.

## Azure Services Used
- Azure Virtual Machines
- log analytics workspace
- Sentinel
- Azure Moniter
- Virtual Network
- NSG
- Azure subcribition
  
## Step 1: Setting Up the Virtual Machines (VMs)

### Resource Group and Virtual Network

- **Resource Group Name:** `cybersecurity`
- **Virtual Network Name:** `cyber-vnet`
  

I created a Resource Group named `cybersecurity` and then set up a Virtual Network (VNet) named `cyber-vnet` within the same Resource Group. This VNet was configured to host both the Windows and Linux VMs.

### Creating the Virtual Machines

- **Windows VM:**
  - **VM Name:** `windows-vm`
  - **OS:** Windows Server 2019
  - **Size:** Standard B2ms
  - **Public IP:** Enabled
  - **VNet/Subnet:** `cyber-vnet`/`default`
  - **NSG:** Configured to allow inbound traffic on all ports (temporarily for attracting attackers).

- **Linux VM:**
  - **VM Name:** `linux`
  - **OS:** Ubuntu 20.04 LTS
  - **Size:** Standard B2ms
  - **Public IP:** Enabled
  - **VNet/Subnet:** `cyber-vnet`/`default`
  - **NSG:** Configured similarly to the Windows VM, allowing inbound traffic on all ports.

## Step 2: Configuring the Network Security Groups (NSGs)

To make the VMs attractive targets for attackers, I configured the NSGs associated with both VMs to allow inbound traffic on all ports. This setup was intentional to collect data on potential security breaches, such as unauthorized login attempts and network scanning activities.

## Step 3: Creating and Connecting Log Analytics Workspace

### Log Analytics Workspace

- **Workspace Name:** `loganalyser`

I created a Log Analytics Workspace named `loganalyser` within the `cybersecurity` Resource Group. The primary purpose of this workspace was to collect and analyze logs from both VMs.

### Connecting VMs to Log Analytics Workspace

- **For Windows VM (`windows-vm`):**
  - Installed the Log Analytics agent on the VM.
  - Connected the VM to the `loganalyser` workspace using the agent.

- **For Linux VM (`linux`):**
  - Installed the Log Analytics agent on the VM.
  - Connected the VM to the `loganalyser` workspace.

By connecting both VMs to the Log Analytics Workspace, I ensured that all activities on these machines were logged and could be analyzed using Azure's powerful querying capabilities.

### Extracting IP Addresses and Location Information
**I utilized a Python script to extract IP addresses from the event logs and retrieve location information for these IPs.**

Python Script:
The script performed the following tasks:

**Extract IP Addresses: Extracted IP addresses from the event logs using regular expressions.
Fetch Location Information: Used the ip-api.com service to obtain geographic information (country, latitude, longitude) for each IP address.
Export Results: Saved the extracted IP addresses and their location details to a CSV file.**

## Step 4: Setting Up Azure Sentinel

Azure Sentinel was set up within the same Resource Group (`cybersecurity`) to monitor the logs collected in the `loganalyser` workspace.

### Steps:

- **Create Sentinel Instance:**
  - Go to the `loganalyser` workspace in the Azure Portal.
  - Enable Azure Sentinel on this workspace.

- **Data Connector Configuration:**
  - Configure data connectors in Azure Sentinel to ingest data from the connected VMs.

- **Workbook and Visualization:**
  - In Sentinel, I created a custom Workbook to visualize the collected data.
  - Specifically, I set up a map visualization that plotted events such as login attempts and suspicious network activities.

## Step 5: Data Collection and Analysis

I left the VMs running for a full day to allow sufficient data collection. During this period, the NSGs were configured to allow all inbound traffic, which led to numerous login attempts and other network activities being logged.

### Data Analysis:

- Using Azure Sentinel and Log Analytics, I queried the logs to identify patterns of suspicious activities.
- The map visualization in the Workbook provided a geographic representation of where the attacks were originating.
- 
  ![rdp](https://github.com/user-attachments/assets/9c2e3c56-1b77-49a2-a539-9870100e8a89)

 ### Overall login attempts Recorded

 ![overall](https://github.com/user-attachments/assets/bca3bfe6-0041-4fe4-8d68-3d0482d570bd)

## Step 6: Enhancing Security Posture

After collecting data for one day, I reconfigured the NSG rules to harden the security of the VMs:

### Updated NSG Rules:

- Restricted inbound traffic to only necessary ports (e.g., SSH for Linux and RDP for Windows).
- Implemented IP whitelisting to allow access only from trusted sources.
  
| Metric                   | Change After NSG
| ------------------------ | -----
| SecurityEvent            | 0%
| Syslog                   | 0%


### Monitoring the Impact:

- Post-configuration, the number of attacks dropped by 99%, highlighting the effectiveness of the new security rules.

## Conclusion and Future Enhancements

This project demonstrated how Azure's integrated services could be used to set up a real-world cybersecurity monitoring environment. The combination of Virtual Machines, Log Analytics, and Azure Sentinel provided a robust framework for detecting and responding to potential threats.

| Metric                                       | Query                                                                                                                                            |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Security Events (Windows VMs)                | SecurityEvent<br>\| where TimeGenerated>= ago(24h)<br>\| count                                                                                   |
| Syslog (Linux VMs)                           | Syslog<br>\| where TimeGenerated >= ago(24h)<br>\| count  

![cybersecurity](https://github.com/user-attachments/assets/4372678d-9730-4d99-bce9-a88849172df4)


