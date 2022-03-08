# PortFlooder

- This is a script that flood packets to a port on the ip you want, and the number of packets you want!

for example you type this on the script:

![](https://data.terabox.com/thumbnail/af2253631d470e7e907745e1262e70f3?fid=4400373096117-250528-606988589247024&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-TdVHbioB%2bnfmEKkCRClciTmj5ps%3d&expires=8h&chkbd=0&chkv=0&dp-logid=406999160019120190&dp-callid=0&time=1646776800&size=c1519_u858&quality=90&vuk=4400373096117&ft=image&autopolicy=1)

The program will flood **just** the port 80, and "Number of packets" times.

Output:

![](https://data.terabox.com/thumbnail/66aff01523af620d5f6a48f91fe64501?fid=4400373096117-250528-102310151284878&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-dxlLUPtwTzrYdIaUqZfvHMgG39w%3d&expires=8h&chkbd=0&chkv=0&dp-logid=407119955811092633&dp-callid=0&time=1646776800&size=c1519_u858&quality=90&vuk=4400373096117&ft=image&autopolicy=1)

I did the test and checked the impact on wireshark

![](https://data.terabox.com/thumbnail/064282fd08bf89b6fd4c67d3f936d198?fid=4400373096117-250528-50496547601058&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-o0yC7QObWgnJP%2bzEtSGWxJSevUE%3d&expires=8h&chkbd=0&chkv=0&dp-logid=407162261710201348&dp-callid=0&time=1646776800&size=c1519_u858&quality=90&vuk=4400373096117&ft=image&autopolicy=1)

As you can see, the wireshark detected it as unreachable port,this is because i dont have a service running at port 80...but.. all packets are here, the script works!
