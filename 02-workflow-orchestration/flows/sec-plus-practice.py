"""
76)[Verified]
Select the appropriate attack and remediation from each drop-down list to label the corresponding attack with its remediation.

Attack Description: An attacker sends multiple SYN packets from multiple sources.
Target: Web server      
Attack Identified: *Botnet, RAT, Logic Bomb, Backdoor, Virus, Spyware, Worm, Adware, Randsomware, Keylogger, Phishing.   
Best Preventative or Remediation Action:
   *Enable DDOS protection,
    Patch vulnerable systems,
    Disable vulnerable services,
    Change the default system password
    Update the cyptographic algorythims
    Change the default application password
    Implement 2FA using push notification
    Conduct a code review
    Implement application fuzzing
    Implement a host-based IPS
    Disable remote access services

Attack Description: The attack establishes a connection. Which allows remote commands to be executed.
Target: User      
Attack Identified: Botnet, *RAT, Logic Bomb, Backdoor, Virus, Spyware, Worm, Adware, Randsomware, Keylogger, *Phishing.   
Best Preventative or Remediation Action:
    Enable DDOS protection,
    Patch vulnerable systems,
    Disable vulnerable services,
    Change the default system password
    Update the cyptographic algorythims
    Change the default application password
    Implement 2FA using push notification
    Conduct a code review
    Implement application fuzzing
   *Implement a host-based IPS
    Disable remote access services

Attack Description: The attack is self propagating and compromises a SQL database using well-known credentials as it moves through the network .
Target: Database server      
Attack Identified: Botnet, RAT, Logic Bomb, Backdoor, Virus, Spyware, *Worm, Adware, Randsomware, Keylogger, Phishing.   
Best Preventative or Remediation Action:
    Enable DDOS protection,
   *Patch vulnerable systems,
    Disable vulnerable services,
    Change the default system password
    Update the cyptographic algorythims
   *Change the default application password
    Implement 2FA using push notification
    Conduct a code review
    Implement application fuzzing
    Implement a host-based IPS
    Disable remote access services

Attack Description: The attacker uses hardware to remotely monitor a user's input activity to harvest credentials.
Target: Executive      
Attack Identified: Botnet, RAT, Logic Bomb, Backdoor, Virus, Spyware, Worm, Adware, Randsomware, *Keylogger, Phishing.   
Best Preventative or Remediation Action:
    Enable DDOS protection,
    Patch vulnerable systems,
    Disable vulnerable services,
    Change the default system password
    Update the cyptographic algorythims
    Change the default application password
   *Implement 2FA using push notification
    Conduct a code review
    Implement application fuzzing
    Implement a host-based IPS
    Disable remote access services

Attack Description: The attacker embeds hidden acces in an internally developed application that bypasses account login.
Target: Application      
Attack Identified: Botnet, RAT, Logic Bomb, *Backdoor, Virus, Spyware, Worm, Adware, Randsomware, Keylogger, Phishing.   
Best Preventative or Remediation Action:
    Enable DDOS protection,
    Patch vulnerable systems,
    Disable vulnerable services,
    Change the default system password
    Update the cyptographic algorythims
    Change the default application password
    Implement 2FA using push notification
   *Conduct a code review
    Implement application fuzzing
    Implement a host-based IPS
    Disable remote access services

77) [Verified] You are a security administrator investigating a potential infection on a network.
Review all logs to determine which host originated the infection and then identify if each remaining host is clean or infected.

__ 192.168.10.22 __
4/17/2019  14:30  Info   Scheduled scan initiated
4/17/2019  14:31  Info   Checking for update
4/17/2019  14:32  Info   No update available
4/17/2019  14:33  Info   Checking for definition update
4/17/2019  14:34  Info   No definition update available
4/17/2019  14:35  Info   Scan type = full
4/17/2019  14:36  Info   Scan start
4/17/2019  14:37  Info   Scanning system files
4/17/2019  14:38  Info   Scanning temporary files
4/17/2019  14:39  Info   Scanning services
4/17/2019  14:40  Info   Scanning boot sector
4/17/2019  14:41  Info   Scan complete
4/17/2019  14:42  Info   Files removed: 0
4/17/2019  14:43  Info   Files quarantined: 0
4/17/2019  14:44  Info   Boot sector: clean
4/17/2019  14:45  Info   Next Scheduled scan: 4/18/2019 14:30
4/18/2019  2:31   Warn   Scheduled scan disabled be process scvh0st.exe
4/18/2019  2:32   Warn   Scheduled update disabled by process scvh0st.exe

__ 192.168.10.37 __
4/17/2019  14:30  Info   Scheduled scan initiated
4/17/2019  14:31  Info   Checking for update
4/17/2019  14:32  Info   No update available
4/17/2019  14:33  Info   Checking for definition update
4/17/2019  14:34  Info   No definition update available
4/17/2019  14:35  Info   Scan type = full
4/17/2019  14:36  Info   Scan start
4/17/2019  14:37  Info   Scanning system files
4/17/2019  14:38  Info   Scanning temporary files
4/17/2019  14:39  Info   Scanning services
4/17/2019  14:40  Info   Scanning boot sector
4/17/2019  14:41  Info   Scan complete
4/17/2019  14:42  Info   Files removed: 0
4/17/2019  14:43  Info   Files quarantined: 0
4/17/2019  14:44  Info   Boot sector: clean
4/17/2019  14:45  Info   Next Scheduled scan: 4/18/2019 14:30
4/18/2019  14:30  Info   Scheduled scan initiated
4/18/2019  14:31  Info   Checking for update
4/18/2019  14:32  Info   update available
4/18/2019  14:33  Info   Checking for definition update
4/18/2019  14:34  Info   Update available v10.2.3.4440
4/18/2019  14:33  Info	 Downloading update
4/18/2019  14:35  Info   Definition update complete
4/18/2019  14:35  Info   Scan type = full
4/18/2019  14:36  Info	 Scan start
4/18/2019  14:37  Info   Scanning system files
4/18/2019  14:37  Warn 	 File found svch0st.exe match definition v10.2.3.4440
4/18/2019  14:37  Warn 	 File quarantined svch0st.exe
4/18/2019  14:38  Info   Scanning temporary files
4/18/2019  14:39  Info   Scanning services
4/18/2019  14:40  Info   Scanning boot sector
4/18/2019  14:41  Info   Scan complete
4/18/2019  14:42  Info   Files removed: 0
4/18/2019  14:43  Info   Files quarantined: 1
4/18/2019  14:44  Info   Boot sector: clean
4/18/2019  14:45  Info   Next Scheduled scan: 4/19/2019 14:30

__ 192.168.10.41 __
4/17/2019  14:30  Info   Scheduled scan initiated
4/17/2019  14:31  Info   Checking for update
4/17/2019  14:32  Info   No update available
4/17/2019  14:33  Info   Checking for definition update
4/17/2019  14:34  Info   No definition update available
4/17/2019  14:35  Info   Scan type = full
4/17/2019  14:36  Info   Scan start
4/17/2019  14:37  Info   Scanning system files
4/17/2019  14:38  Info   Scanning temporary files
4/17/2019  14:39  Info   Scanning services
4/17/2019  14:40  Info   Scanning boot sector
4/17/2019  14:41  Info   Scan complete
4/17/2019  14:42  Info   Files removed: 0
4/17/2019  14:43  Info   Files quarantined: 0
4/17/2019  14:44  Info   Boot sector: clean
4/17/2019  14:45  Info   Next Scheduled scan: 4/18/2019 14:30
4/18/2019  14:30  Info   Scheduled scan initiated
4/18/2019  14:31  Info   Checking for update
4/18/2019  14:32  Info   No update available
4/18/2019  14:33  Info   Checking for definition update
4/18/2019  14:34  Error  Unable to reach update server
4/18/2019  14:35  Info   Scan type = full
4/18/2019  14:36  Info	 Scan start
4/18/2019  14:37  Info	 Scanning system files
4/18/2019  14:37  Warn	 File found svch0st.exe match definition v10.2.3.4440
4/18/2019  14:37  Error	 Unable to quarantined file svch0st.exe
4/18/2019  14:37  Info   Scanning temporary files
4/18/2019  14:39  Info   Scanning services
4/18/2019  14:40  Info   Scanning boot sector
4/18/2019  14:41  Info   Scan complete
4/18/2019  14:42  Info   Files removed: 0
4/18/2019  14:43  Info   Files quarantined: 0
4/18/2019  14:43  Warn   File quarantine file
4/18/2019  14:44  Info   Boot sector: clean
4/18/2019  14:45  Info   Next Scheduled scan: 4/19/2019 14:30

__ 10.10.9.12 __
4/17/2019  14:30  Info   Scheduled scan initiated
4/17/2019  14:31  Info   Checking for update
4/17/2019  14:32  Info   No update available
4/17/2019  14:33  Info   Checking for definition update
4/17/2019  14:34  Info   No definition update available
4/17/2019  14:35  Info   Scan type = full
4/17/2019  14:36  Info   Scan start
4/17/2019  14:37  Info   Scanning system files
4/17/2019  14:38  Info   Scanning temporary files
4/17/2019  14:39  Info   Scanning services
4/17/2019  14:40  Info   Scanning boot sector
4/17/2019  14:41  Info   Scan complete
4/17/2019  14:42  Info   Files removed: 0
4/17/2019  14:43  Info   Files quarantined: 0
4/17/2019  14:44  Info   Boot sector: clean
4/17/2019  14:45  Info   Next Scheduled scan: 4/18/2019 14:30
4/18/2019  14:30  Info   Scheduled scan initiated
4/18/2019  14:31  Info   Checking for update
4/18/2019  14:32  Info   update available
4/18/2019  14:33  Info   Checking for definition update
4/18/2019  14:34  Info   Update available v10.2.3.4440
4/18/2019  14:33  Info	 Downloading update
4/18/2019  14:35  Info   Definition update complete
4/18/2019  14:35  Info   Scan type = full
4/18/2019  14:36  Info	 Scan start
4/18/2019  14:37  Info   Scanning system files
4/18/2019  14:37  Warn 	 File found svch0st.exe match definition v10.2.3.4440
4/18/2019  14:37  Warn 	 File quarantined svch0st.exe
4/18/2019  14:38  Info   Scanning temporary files
4/18/2019  14:39  Info   Scanning services
4/18/2019  14:40  Info   Scanning boot sector
4/18/2019  14:41  Info   Scan complete
4/18/2019  14:42  Info   Files removed: 0
4/18/2019  14:43  Info   Files quarantined: 1
4/18/2019  14:44  Info   Boot sector: clean
4/18/2019  14:45  Info   Next Scheduled scan: 4/19/2019 14:30

__ 10.10.9.18 __
4/17/2019  14:30  Info   Scheduled scan initiated
4/17/2019  14:31  Info   Checking for update
4/17/2019  14:32  Info   No update available
4/17/2019  14:33  Info   Checking for definition update
4/17/2019  14:34  Info   No definition update available
4/17/2019  14:35  Info   Scan type = full
4/17/2019  14:36  Info   Scan start
4/17/2019  14:37  Info   Scanning system files
4/17/2019  14:38  Info   Scanning temporary files
4/17/2019  14:39  Info   Scanning services
4/17/2019  14:40  Info   Scanning boot sector
4/17/2019  14:41  Info   Scan complete
4/17/2019  14:42  Info   Files removed: 0
4/17/2019  14:43  Info   Files quarantined: 0
4/17/2019  14:44  Info   Boot sector: clean
4/17/2019  14:45  Info   Next Scheduled scan: 4/18/2019 14:30
4/18/2019  14:30  Info   Scheduled scan initiated
4/18/2019  14:31  Info   Checking for update
4/18/2019  14:32  Info   No update available
4/18/2019  14:33  Info   Checking for definition update
4/18/2019  14:34  Error  Unable to reach update server
4/18/2019  14:35  Info   Scan type = full
4/18/2019  14:36  Info	 Scan start
4/18/2019  14:37  Info	 Scanning system files
4/18/2019  14:37  Warn	 File found svch0st.exe match definition v10.2.3.4440
4/18/2019  14:37  Error	 Unable to quarantined file svch0st.exe
4/18/2019  14:38  Info   Scanning temporary files
4/18/2019  14:39  Info   Scanning services
4/18/2019  14:40  Info   Scanning boot sector
4/18/2019  14:41  Info   Scan complete
4/18/2019  14:42  Info   Files removed: 0
4/18/2019  14:43  Info   Files quarantined: 0
4/18/2019  14:43  Warn   File quarantine file
4/18/2019  14:44  Info   Boot sector: clean
4/18/2019  14:45  Info   Next Scheduled scan: 4/19/2019 14:30

__ Firewall __
Timestamp             Source         Destination    Destination Port  Application   Action  Client Bytes   Server Bytes
4/17/2019  16:01:44   10.10.9.18     57.203.54.183  443               ssl           Permit  6953           99427
4/17/2019  16:01:58   192.168.10.37  57.203.54.221  443               ssl           Permit  9301           199386
4/17/2019  16:17:06   192.168.10.22  10.10.9.12     135               rpc           Permit  175            1504
4/17/2019  16:27:36   192.168.10.41  10.10.9.12     445               smbv1         Permit  345            34757
4/17/2019  16:28:06   10.10.9.12     192.168.10.41  135               rpc           Permit  754            4771
4/17/2019  16:33:31   10.10.9.18     192.168.10.22  135               rpc           Permit  643            2355
4/17/2019  16:35:36   192.168.10.37  10.10.9.12     135               smbv2         Permit  649            5644
4/17/2019  23:58:36   10.10.9.12     192.168.10.41                    icmp          Permit  128            128
4/17/2019  23:58:43   10.10.9.12     192.168.10.22                    icmp          Permit  128            128
4/17/2019  23:58:45   10.10.9.12     192.168.10.37                    icmp          Permit  128            128
4/18/2019  2:31:36    10.10.9.18     192.168.10.41  445               smbv2         Permit  1874           23874
4/18/2019  2:31:45    192.168.10.22  57.203.55.29   8080              http          Permit  7203           75997
4/18/2019  2:31:51    10.10.9.18     57.203.56.201  443               ssl           Permit  9953           199730
4/18/2019  2:31:02    192.168.10.22  57.203.55.234  443               http          Permit  4937           84937
4/18/2019  2:39:11    192.168.10.41  57.203.53.89   8080              http          Permit  8201           133183
4/18/2019  2:39:12    10.10.9.18     57.203.55.19   8080              ssl           Permit  1284           9102854
4/18/2019  2:39:32    192.168.10.37  57.203.56.113  443               ssl           Permit  9341           9938
4/18/2019  13:37:36   192.168.10.22  10.10.9.18     445               smbv3         Permit  1874           23874
4/18/2019  13:39:43   192.168.10.22  10.10.9.18     135               rpc           Permit  673            41358
4/18/2019  13:45:04   10.10.9.18     192.168.10.37  135               rpc           Permit  693            1952
4/18/2019  13:47:44   10.10.9.12     192.168.10.41  445               smbv3         Permit  482            3505
4/18/2019  13:52:57   10.10.9.12     192.168.10.22  135               rpc           Permit  545            90063
4/18/2019  13:53:01   192.168.10.37  10.10.9.12     335               smbv3         Permit  876            8068
4/18/2019  14:30:04   10.10.9.12     57.203.56.231  443               ssl           Permit  9901           199730
4/18/2019  14:30:04   192.168.10.37  57.203.56.143  443               ssl           Permit  10092          209938


192.168.10.22; *Origin, *Infected, Clean
192.168.10.37; Origin, Infected, *Clean
192.168.10.41; Origin, *Infected, Clean

10.10.9.12; Origin, Infected, *Clean
10.10.9.18; Origin, *Infected, Clean

78) 
Which of the following is the phase in the incident response process when a security analyst reviews roles and responsibilities?
C. Lessons learned

79)
After a recent vulnerability scan, a security engineer needs to harden the routers within the corporate network. 
Which of the following is the most appropriate to disable?
D. Web-based administration

80)
A security administrator needs a method to secure data in an environment that includes some form of checks so track any changes. 
Which of the following should the administrator set up to achieve this goal?
D. FIM (File Integrity Monitoring)

81)

An administrator is reviewing a single server's security logs and discovers the following:
Keywords        Date and Time            Source                      Event ID   Task Category
Audit Failure   09/16/2022 11:13:05 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:07 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:09 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:11 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:13 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:15 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:17 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:19 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:21 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:23 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:25 AM   Microsoft Windows Security  4625       Logon
Audit Failure   09/16/2022 11:13:27 AM   Microsoft Windows Security  4625       Logon

Which of the following best describes the action captured in this log file?

82)
A security engineer is implementing FDE for all laptops in an organization. 
Which of the following are the most important for the engineer to consider as part of the planning process? (Choose two.)

A. Key escrow
B. TPM presence

83)
A security analyst scans a company's public network and discovers a host is running a remote desktop that can be used to access the production network. 
Which of the following changes should the security analyst recommend?

B. Setting up a VPN and placing the jump server inside the firewall

84)
An enterprise has been experiencing attacks focused on exploiting vulnerabilities in older browser versions with well-known exploits. 
Which of the following security solutions should be configured to best provide the ability to monitor and block these known signature-based attacks?

D. IPS (Intrusion Prevention System) → Detects and actively blocks attacks using signatures.

85)
Security controls in a data center are being reviewed to ensure data is properly protected and that human life considerations are included. 
Which of the following best describes how the controls should be set up?

C. Safety controls should fail open

86)
Which of the following would be best suited for constantly changing environments?

B. Containers

87)
Which of the following incident response activities ensures evidence is properly handled?

88)
An accounting clerk sent money to an attacker's bank account after receiving fraudulent instructions to use a new account. 
Which of the following would most likely prevent this activity in the future?

D. Updating processes for sending wire transfers

89)
A systems administrator is creating a script that would save time and prevent human error when performing account creation for a large number of end users. 
Which of the following would be a good use case for this task?

B. Orchestration

90)
A company's marketing department collects, modifies, and stores sensitive customer data. The infrastructure team is responsible for securing the data while in transit and at rest. 
Which of the following data roles describes the customer?

C. Subject

91)
Which of the following describes the maximum allowance of accepted risk?

D. Risk threshold

92)
A security analyst receives alerts about an internal system sending a large amount of unusual DNS queries to systems on the internet over short periods of time during non-business hours. 
Which of the following is most likely occurring?

B. Data is being exfiltrated.

93) [Verified]
A technician is opening ports on a firewall for a new system being deployed and supported by a SaaS provider. 
Which of the following is a risk in the new system?

C. Supply chain vendor

94)
A systems administrator is working on a solution with the following requirements:
•Provide a secure zone.
•Enforce a company-wide access control policy.
•Reduce the scope of threats.
Which of the following is the systems administrator setting up?

A. Zero Trust

95)
Which of the following involves an attempt to take advantage of database misconfigurations?

B. SQL injection

96)
Which of the following is used to validate a certificate when it is presented to a user?

A. OCSP (Online Certificate Status Protocol)

97)
One of a company's vendors sent an analyst a security bulletin that recommends a BIOS update. 
Which of the following vulnerability types is being addressed by the patch?

B. Firmware

98)
Which of the following is used to quantitatively measure the criticality of a vulnerability?

B. CVSS (Common Vulnerability Scoring System)  Provides a numerical severity score

99)
Which of the following actions could a security engineer take to ensure workstations and s
ervers are properly monitored for unauthorized changes and software?

D. Install endpoint management software on all systems

100)
An organization is leveraging a VPN between its headquarters and a branch location. 
Which of the following is the VPN protecting?

B. Data in transit

101) 
Which biometric error would allow an unauthorized user to access a system?

A. False acceptance


102) 
A company is auditing the manner in which its European customers' personal information is handled. 
Which of the following should the company consult?

A. GDPR (General Data Protection Regulation) is a regulation in EU law on data protection and privacy.

103) 
Which of the following describes the exploitation of an interactive process to gain access to restricted areas?

C. Privilege escalation

104) 
An organization is planning to open other data centers to sustain operations in the event of a natural disaster. 
Which of the following considerations would BEST support the organization's resiliency?

A. Geographic dispersal

105) An organization has decided to purchase an insurance policy because a risk assessment determined that
 the cost to remediate the risk is greater than the five- year cost of the insurance policy. 
The organization is enabling risk:

D. transference.

106) The Chief Information Security Officer (CISO) requested a report on potential areas of improvement following a security incident.
 Which of the following incident response processes is the CISO requesting?

A .Lessons learned

107) 
A company is providing security awareness training regarding the importance of not forwarding social media messages from unverified sources. 
Which of the following risks would this training help to prevent?

A. Hoaxes

108) A security analyst is receiving numerous alerts reporting that the response time of an internet-facing application has been degraded. 
However, the internal network performance was not degraded. Which of the following MOST likely explains this behavior?

C. DDoS attack

109) 
Which of the following will increase cryptographic security?

A. High data entropy

110) 
Which of the following statements BEST describes zero-day exploits?

C. A zero-day exploit is initially undetectable, and no patch for it exists.

111) 
A company wants to restrict emailing of PHI documents. The company is implementing a DLP solution. 
In order to restrict PHI documents, which of the following should be performed FIRST?

C. Classification

112) 
Which of the following describes the continuous delivery software development methodology?

D. Agile

113) 
A company suspects that some corporate accounts were compromised. 
The number of suspicious logins from locations not recognized by the users is increasing.
Employees who travel need their accounts protected without the risk of blocking legitimate login requests that may be made over new sign-in properties. 
Which of the following security controls can be implemented?

A. Enforce MFA when an account request reaches a risk threshold.

114) 
An organization wants to participate in threat intelligence information sharing with peer groups. 
Which of the following would MOST likely meet the organization's requirement

D.Implement a TAXII server.

115) 
Which of the following is the GREATEST security concern when outsourcing code development to third-party contractors for an internet-facing application?

C. Unknown backdoor

116) 
An amusement park is implementing a biometric system that validates customers' fingerprints to ensure they are not sharing tickets. The park's owner values customers above all and would prefer customers' convenience over security. 
For this reason, which of the following features should the security team prioritize FIRST?

C. Low FRR (False Rejection Rate)

117) 
Which of the following organizations sets frameworks and controls for optimal security configuration on systems?

D. NIST (National Institute of Standards and Technology) develops cybersecurity standards, guidelines, and best practices.

118) 
An organization discovered files with proprietary financial data have been deleted. 
The files have been recovered from backup, but every time the Chief FinancialOfficer logs in to the file server, the same files are deleted again. 
No other users are experiencing this issue. 
Which of the following types of malware is MOST likely causing this behavior?

A.
Logic bomb

119) 
A security analyst has identified malware spreading through the corporate network and has activated the CSIRT. 
Which of the following should the analyst do NEXT?

B. Attempt to quarantine all infected hosts to limit further spread.

121) 
A recent security breach exploited software vulnerabilities in the firewall and within the network management solution. 
Which of the following will MOST likely be used to identify when the breach occurred through each device?

A. SIEM correlation dashboards

122) 
A cloud service provider has created an environment where customers can connect existing local networks to the cloud for additional computing resources and 
block internal HR applications from reaching the cloud. 
Which of the following cloud models is being used?

C. Hybrid

123) 
A security analyst is working on a project to implement a solution that monitors network communications and 
provides alerts when abnormal behavior is detected.Which of the following is the security analyst MOST likely implementing?

B. User behavior analysis

124) 
Data exfiltration analysis indicates that an attacker managed to download system configuration notes from a web server. 
The web-server logs have been deleted, but analysts have determined that the system configuration notes were stored in the database administrator's folder on the web server. 
Which of the following attacks explains what occurred? (Choose two.)

B. Directory traversal
D. Privilege escalation

125) 
A junior security analyst is conducting an analysis after passwords were changed on multiple accounts without users' interaction. 
The SIEM have multiple login entries with the following text: 
suspicious event - user: scheduledtasks successfully authenticate on AD on abnormal time 
suspicious event - user: scheduledtasks failed to execute c:\weekly_checkups\amazing-3rdparty-domain-assessment.py 
suspicious event - user: scheduledtasks failed to execute c:\weekly_checkups\secureyourAD-3rdparty-compliance.sh 
suspicious event - user: scheduledtasks successfully executed c:\weekly_checkups\amazing-3rdparty-domain-assessment.py 
Which of the following is the MOST likely attack conducted on the environment?

A. Malicious script

126) 
A customer service representative reported an unusual text message that was sent to the help desk. 
The message contained an unrecognized invoice number with a large balance due and a link to click for more details. 
Which of the following BEST describes this technique?

D. Smishing

127) 
Which of the following actions would be recommended to improve an incident response process?

A. Train the team to identify the difference between events and incidents.

128) 
A cybersecurity administrator needs to implement a Layer 7 security control on a network and block potential attacks. 
Which of the following can block an attack atLayer 7? (Choose two.)

B. NIPS (Network Intrusion Prevention System)
D. WAF (Web Application Firewall)

129) 
A business operations manager is concerned that a PC that is critical to business operations will have a costly hardware failure soon. 
The manager is looking for options to continue business operations without incurring large

B. Perform a physical-to-virtual migration.

130) 
An organization has activated an incident response plan due to a malware outbreak on its network. 
The organization has brought in a forensics team that has identified an internet-facing Windows server as the likely point of initial compromise. 
The malware family that was detected is known to be distributed by manually logging on to servers and running the malicious code. 
Which of the following actions would be BEST to prevent reinfection from the infection vector?

130) 
An organization has activated an incident response plan due to a malware outbreak on its network. 
The organization has brought in a forensics team that has identified an internet-facing Windows server as the likely point of initial compromise. 
The malware family that was detected is known to be distributed by manually logging on to servers and running the malicious code. 
Which of the following actions would be BEST to prevent reinfection from the infection vector?

D. Block port 3389 inbound from untrusted networks.

131) 
Which of the following uses SAML for authentication?

B. Federation

132) 
The SOC for a large MSSP is meeting to discuss the lessons learned from a recent incident that took much too long to resolve. 
This type of incident has become more common in recent weeks and is consuming large amounts of the analysts' time due to manual tasks being performed. 
Which of the following solutions should the SOC consider to BEST improve its response time?

C. Implement a SOAR with customizable playbooks.

133) Business partners are working on a security mechanism to validate transactions securely. 
The requirement is for one company to be responsible for deploying a trusted solution that will register and issue artifacts used to sign,
 encrypt, and decrypt transaction files. 
Which of the following is the BEST solution to adopt?

A. PKI (Public Key Infrastructure) is a framework for managing digital certificates and public-key encryption.

134) A security analyst has been asked by the Chief Information Security Officer to: 
-develop a secure method of providing centralized management of infrastructure 
-reduce the need to constantly replace aging end user machines 
-provide a consistent user desktop experienceWhich of the following BEST meets these requirements?

C. VDI

135) 
Which of the following terms describes a broad range of information that is sensitive to a specific organization?

C. Proprietary

136) 
A security manager has tasked the security operations center with locating all web servers that respond to an unsecure protocol. 
Which of the following commands could an analyst run to find the requested servers?

B. nmap -p 80 10.10.10.0/24


137) 
Which of the following is a reason to publish files' hashes?

A. To validate the integrity of the files

138)
A company recently experienced an inside attack using a corporate machine that resulted in data compromise. 
Analysis indicated an unauthorized change to the software circumvented technological protection measures. 
The analyst was tasked with determining the best method to ensure the integrity of the systems remains intact and local and remote boot attestation can take place. 
Which of the following would provide the BEST solution?

139) A user enters a username and a password at the login screen for a web portal. 
A few seconds later the following message appears on the screen:Please use a combination of numbers, special characters,
 and letters in the password field.
Which of the following concepts does this message describe?

A. Password complexity

140) 
Which of the following would be indicative of a hidden audio file found inside of a piece of source code?

A. Steganography

141) 
An administrator needs to protect user passwords and has been advised to hash the passwords. 
Which of the following BEST describes what the administrator is being advised to do?

A. Perform a mathematical operation on the passwords that will convert them into unique strings.

142) 
A security engineer is building a file transfer solution to send files to a business partner. 
The users would like to drop off the files in a specific directory and have the server send the file to the business partner. 
The connection to the business partner is over the internet and needs to be secure. 
Which of the following can be used?

C. SSH

143) 
Which of the following can be used by a monitoring tool to compare values and detect password leaks without providing the actual credentials?

A. Hashing

144) 
Several attempts have been made to pick the door lock of a secure facility. 
As a result, the security engineer has been assigned to implement a stronger preventative access control. 
Which of the following would BEST complete the engineer's assignment?

A. Replacing the traditional key with an RFID key


145) 
Which of the following is an effective tool to stop or prevent the exfiltration of data from a network?

A. DLP (Data Loss Prevention) is a strategy for preventing sensitive data from leaving the network.

146) A company wants to simplify the certificate management process. 
The company has a single domain with several dozen subdomains, all of which are publicly accessible on the internet. 
Which of the following BEST describes the type of certificate the company should implement?

B. Wildcard certificate

147) 
A report delivered to the Chief Information Security Officer (CISO) shows that some user credentials could be exfiltrated. 
The report also indicates that users tend to choose the same credentials on different systems and applications. 
Which of the following policies should the CISO use to prevent someone from using the exfiltrated credentials?

A. MFA (Multi-Factor Authentication) requires users to provide multiple forms of verification, making it more difficult for attackers to use stolen credentials.

148) 
A company is implementing a DLP solution on the file server. 
The file server has PII, financial information, and health information stored on it. 
Depending on what type of data that is hosted on the file server, the company wants different DLP rules assigned to the data. 
Which of the following should the company do to help accomplish this goal?

A. Classify the data.

149) 
A security analyst is reviewing application logs to determine the source of a breach and locates the 
following log: https://www.comptia.com/login.php?id='%20or%20'1'1='1 
Which of the following has been observed?

C. SQLi is a code injection technique that exploits vulnerabilities in an application's software by inserting malicious SQL statements into input fields.

150) 
Which of the following tools is effective in preventing a user from accessing unauthorized removable media?

A. USB data blocker

151) 
A user is attempting to navigate to a website from inside the company network using a desktop. 
When the user types in the URL, https://www.site.com, the user is presented with a certificate mismatch warning from the browser. 
The user does not receive a warning when visiting http://www.anothersite.com. 
Which of the following describes this attack?

A. On-path attack , Another name for man-in-the-middle

152) A Chief Security Officer is looking for a solution that can provide increased scalability and flexibility for back-end infrastructure, 
allowing it to be updated and modified without disruption to services. 
The security architect would like the solution selected to reduce the back-end server resources and has highlighted that session persistence 
is not important for the applications running on the back-end servers. 
Which of the following would BEST meet the requirements?

A. Reverse proxy

153) 
Which of the following describes a social engineering technique that seeks to exploit a person's sense of urgency?

A. A phishing email stating a cash settlement has been awarded but will expire soon

154) An audit identified PII being utilized in the development environment of a critical application. 
The Chief Privacy Officer (CPO) is adamant that this data must be removed; however, the developers are concerned that 
without real data they cannot perform functionality tests and search for specific data. 
Which of the following should a security professional implement to BEST satisfy both the CPO's and the development team's requirements?

A. A phishing email stating a cash settlement has been awarded but will expire soon

154) [Verified]
An audit identified PII being utilized in the development environment of a critical application. 
The Chief Privacy Officer (CPO) is adamant that this data must be removed; however, the developers are concerned that without real data 
they cannot perform functionality tests and search for specific data. 
Which of the following should a security professional implement to BEST satisfy both the CPO's and the development team's requirements?

C. Data masking

155) 
A forensics investigator is examining a number of unauthorized payments that were reported on the company's website. 
Some unusual log entries show users received an email for an unwanted mailing list and clicked on a link to attempt to unsubscribe. 
One of the users reported the email to the phishing team, and the forwarded email revealed the link to be: 
<a href="https://www.company.com/payto.do?routing=00001111&acct=22223334&amount=250">Click here to unsubscribe</a> 
Which of the following will the forensics investigator MOST likely determine has occurred?

D. XSRF "Cross site request forgery (CSRF)"

156) 
Which of the following are common VoIP-associated vulnerabilities? (Choose two.)

A.SPIM
B.Vishing

157) 
A security engineer is deploying a new wireless network for a company. 
The company shares office space with multiple tenants. 
Which of the following should the engineer configure on the wireless network to ensure that confidential data is not exposed to unauthorized users?

A.EAP
B.TLS
C.HTTPS
D.AES











"""