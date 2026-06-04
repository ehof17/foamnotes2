Things are timing out when running the api inside a container.
It can curl to it through
running it with --network=host

It makes the container share the host's network stack directly — no bridge, no NAT, no separate DNS. The container sees the exact same interfaces, IPs, hostname resolution, and routing as siml103 itself.

So wigpu3:6677 resolves exactly the same way it would if you ran the API directly on the box. That's why it tends to fix all three of the issues I listed at once.

The tradeoff: any port the container listens on is exposed directly on the host (no -p mapping needed or possible). Fine for an internal API server, just worth knowing.


Think   it was erroring because of how much friggin stuff we send over http

Container veth interfaces often have MTU 1450 vs the host's 1500. PDF page images sent as base64 are large (potentially several MB) — with an MTU mismatch, these big request bodies can get silently dropped. The fact that smaller pages (2, 3, 1, 6, 4) succeed but image-heavy pages fail is consistent with this. Fix: set --mtu 1450 on your Docker network, or use --network=host.

Quickest fix to confirm/eliminate all of the above: run the container with --network=host and see if the error goes away.

MTU (Maximum Transmission Unit) is the largest chunk of data a network interface will send in a single packet. On most ethernet network it's 1500 bytes.

When Docker creates a bridge network, it sets the container's virtual interface MTU to 1500 by default — but the actual path from the container to the outside world looks like:
container veth → docker0 bridge → host eth0 → network
Each hop through that virtual layer adds overhead (encapsulation headers). So a 1500-byte packet from the container, by the time it's wrapped and sent on the real network, is slightly larger than 1500 bytes — which the physical network rejects.

The network then has to fragment the packet. If fragmentation is blocked (which it often is on corporate networks), the packet just gets silently dropped.

Why 1450 specifically? It's a safe conservative value that leaves room for the overhead added by the bridge/NAT layers. Some people use 1450, some 1460 — the point is just "smaller than 1500 so there's headroom."

Why it matters for your case: normal small requests (JSON, short text) fit in a packet or two and usually survive fragmentation fine. But a PDF page image base64-encoded is potentially several megabytes — thousands of packets — and if even one gets dropped/fragmented badly, the server sees an incomplete request body and closes the connection with no response.

--network=host sidesteps all of this because the container uses the host's real eth0 directly — no virtual bridge, no encapsulation
overhead, MTU is just 1500 end-to-end like normal.
