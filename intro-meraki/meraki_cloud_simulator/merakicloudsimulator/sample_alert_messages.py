alert_messages = {
    "settingsChanged":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:20:39.656975Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "alertId": "0000000000000000",
        "alertType": "Settings changed",
        "occurredAt": "2019-07-19T06:15:33.504142Z",
        "alertData": {
            "name": "Routing and DHCP",
            "url": "/manage/configure/switch_l3",
            "changes": {
            "createStaticRoute": {
                "label": "Added static route on SP-Warehouse",
                "newText": "10.10.10.0/24 -> 172.16.254.253",
                "changedBy": "Miles Meraki (Miles@Meraki.com)",
                "oldText": "",
                "ssidId": None
            }
            },
            "userId": 578149602163763500
        },
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000"
    },
    "vpnConnectivityChanged":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:48:28.731383Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "VPN connectivity changed",
        "occurredAt": "2019-07-19T06:19:23.606000Z",
        "alertData": {
            "vpnType": "l2tpv3",
            "vap": "1",
            "onSecondary": "false",
            "secondaryEndpoint": "0.0.0.0",
            "primaryEndpoint": "1.1.1.1",
            "connectivity": "true"
        }
    },
    "rogueAp":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T05:41:27.939986Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Rogue AP detected",
        "occurredAt": "2011-06-07T01:19:47.432747Z",
        "alertData": {
            "rssi": 1126462856796059000
        }
    },
    "gatewayToRepeater":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T01:23:50.961355Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Gateway to repeater",
        "occurredAt": "2019-07-15T13:55:35.000000Z",
        "alertData": {}
    },
    "failoverEvent":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T01:02:34.397815Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Uplink status changed",
        "occurredAt": "2019-07-19T01:02:01.543000Z",
        "alertData": {
            "uplink": "0"
        }
    },
    "dhcpNoLeases":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T00:47:44.161980Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "DHCP leases exhausted",
        "occurredAt": "2019-07-18T21:41:26.324000Z",
        "alertData": {
            "network": "192.168.1.0/24'192.168.1.254"
        }
    },
    "ipConflict":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T01:28:25.959399Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Client IP conflict detected",
        "occurredAt": "2019-07-19T01:26:43.866000Z",
        "alertData": {
            "conflictingIp": "192.168.1.54",
            "contendingMac": "00:00:00:44:44:44"
        }
    },
    "cellularUpDown":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-18T23:42:26.937287Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Cellular went down",
        "occurredAt": "2019-07-18T22:38:45.429000Z",
        "alertData": {
            "bytesIn": "1861",
            "provider": "AT&amp;amp;T",
            "model": "AirCard 340U",
            "local": "192.168.99.1",
            "remote": "1.1.1.1",
            "connectTime": "2",
            "bytesOut": "1880",
            "connection": "4G"
        }
    },
    "rogueDhcp":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:04:11.110859Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Rogue DHCP server detected",
        "occurredAt": "2019-07-19T01:30:40.382000Z",
        "alertData": {
            "eth": "bb:bb:bb:11:11:11",
            "ip": "10.20.2.62",
            "subnet": "0.0.0.0/0",
            "vlan": "3"
        }
    },
    "vrrp":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:51:37.412365Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Failover event detected",
        "occurredAt": "2019-07-19T05:55:20.524000Z",
        "alertData": {
            "oldIfUp": "0",
            "oldMode": "detect",
            "oldPrio": "75",
            "electorState": "master",
            "mode": "detect",
            "prio": "75",
            "ifUp": "1"
        }
    },
    "ampMalwareBlocked":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-18T22:59:22.887526Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Malware download blocked",
        "occurredAt": "2019-07-18T15:22:53.177000Z",
        "alertData": {}
    },
    "ampMalwareDetected":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-18T22:59:55.022619Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Malware download detected",
        "occurredAt": "2019-07-18T15:29:30.270000Z",
        "alertData": {
            "eventType": "amp_malware_detected",
            "sha256": "ddcb8f357d86d11dfa3409f71a966e5076240445ca9825fb72e7386efc5582e4",
            "disposition": 3
        }
    },
    "newDhcpServer":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T00:45:47.232115Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "New DHCP server detected",
        "occurredAt": "2019-07-19T00:09:17.099000Z",
        "alertData": {
            "mac": "00:00:00:33:33:33",
            "ip": "10.197.134.2",
            "vlan": 104,
            "subnet": "10.197.132.0/24"
        }
    },
    "powerSupplyDown":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T01:52:43.212176Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Power supply went down",
        "occurredAt": "2019-07-18T03:50:28.344000Z",
        "alertData": {
            "num": 2
        }
    },
    "rpsBackup":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:10:01.707366Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "Running on backup power",
        "occurredAt": "2019-06-25T14:59:57.928000Z",
        "alertData": {
            "num": 0
        }
    },
    "udldError":{
        "version": "0.1",
        "sharedSecret": "foo",
        "sentAt": "2019-07-19T06:26:25.538598Z",
        "organizationId": "00000001",
        "organizationName": "Miles Monitoring Inc.",
        "organizationUrl": "https://n1.meraki.com/o//manage/organization/overview",
        "networkId": "N_111111111111",
        "networkName": "Main Office",
        "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
        "deviceSerial": "XXXX-XXXX-XXXX",
        "deviceMac": "00:00:00:aa:bb:cc",
        "deviceName": "Device Foo Bar",
        "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
        "alertId": "0000000000000000",
        "alertType": "UDLD error",
        "occurredAt": "2019-07-18T18:40:25.914000Z",
        "alertData": {
            "errorType": "Unidirectional link (outbound fault)",
            "action": "none",
            "port": {
            "port": 52,
            "moduleSlot": 0,
            "modulePid": ""
            }
        }
    }
}