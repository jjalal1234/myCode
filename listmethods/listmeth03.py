#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
protob = ["ssh", "http", "https"]

print(proto)
print(proto[1])

proto.append('dns')
protoa.append('dns')
protoa.extend([22, 80, 443, 53])

print(proto)
print(protoa)

intList = [22, 80, 443, 53]

protob.append('dns')
protob.append(intList)

print(protob)


