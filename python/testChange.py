from ncclient import manager

m = manager.connect(
    host="sandbox-iosxe-recomm-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    device_params={'name':'csr'}
    )



def netconfChange():
	numberLook = input("masukan number Lookup : ")
	Deskripsi = input("masukan Description : ")
	ipAddress = input("masukan Ip Address : ")
	netMask = input("masukan netmask :")
	CONFIGURATION = f"""
	<config>
		<native
			xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
			<interface>
				<Loopback>
					<name
						xmlns:nc='urn:ietf:params:xml:ns:netconf:base:1.0'>{numberLook}
					</name>
					<description>{Deskripsi}</description>
					<ip>
						<address>
							<primary>
								<address>{ipAddress}</address>
								<mask>{netMask}</mask>
							</primary>
						</address>
					</ip>
				</Loopback>
			</interface>
		</native>
	</config>

	"""

	s = m.edit_config(target = "running", config=CONFIGURATION)
	print(s)
	
# print(m.edit_config(target = "running", config=CONFIGURATION))

	m.close_session()