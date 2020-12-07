maxIps = 10000000
ip_addresses = []

async function gen_ip() {
    i = 0
    while (i != maxIps) {
        i++
        let int1 = Math.floor((Math.random() * 255) + 0);
        let int2 = Math.floor((Math.random() * 168) + 0);
        let int3 = Math.floor((Math.random() * 200) + 0);
        let int4 = Math.floor((Math.random() * 100) + 0);

        let ip_addr = `${int1}.${int2}.${int3}.${int4}`
        if (ip_addresses.includes(ip_addr)) return console.log(`already generated - ${ip_addr}`)
    }

    console.log("done")
}

gen_ip()