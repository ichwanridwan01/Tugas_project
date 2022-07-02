from ncclient import manager

m = manager.connect(
    host="sandbox-iosxe-recomm-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    device_params={'name':'csr'}
    )


def testFilter():
    print("1. mencari Loopback")
    print("2. mencari GigabitEthernet")
    list_pilihan = int(input("Masukan pilihan : "))
    if list_pilihan == 1:
        print("Welcome Loopback")
        search_Lookpback = input("Masukan number : ")

        FILTER_LOOP= f"""
        <filter>
                <native
                    xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                        <Loopback>
                            <name
                                xmlns:nc='urn:ietf:params:xml:ns:netconf:base:1.0'>{search_Lookpback}
                            </name>
                            <description></description>
                            <ip>
                                <address>
                                    <primary>
                                        <address></address>
                                        <mask></mask>
                                    </primary>
                                </address>
                            </ip>
                        </Loopback>
                    </interface>
                </native>
            </filter>

            """

        s = m.get_config("running", filter=FILTER_LOOP)
        print(s)
        print("============================================================")


    elif list_pilihan == 2:
        print("Welcome GigabitEthernet")
        search_gig = input("masukan number GIG \"[1,2,3]\" : ")
        FILTER_GIG = f"""
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <GigabitEthernet>
                        <name xmlns:nc='urn:ietf:params:xml:ns:netconf:base:1.0'>{search_gig}</name>
                        <description></description>
                        <ip>
                            <address>
                                <primary>
                                    <address></address>
                                    <mask></mask>
                                </primary>
                            </address>
                        </ip>
                    </GigabitEthernet>
                </interface>
            </native>
        </filter>

        """
        s = m.get_config("running", filter=FILTER_GIG)
        print(s)
        print("============================================================")
    # print(m.edit_config(target = "running", config=CONFIGURATION))

    m.close_session()

