

deployment_targets = [
    "us-east-1",
"eu-west-1",
"ap-southeast-1"
]

print(deployment_targets)

print(deployment_targets[0])
print(deployment_targets[1])

deployment_targets.append("us-west-2")
print(deployment_targets)

deployment_targets.append("eu-central-1")
print(deployment_targets)

index1 = 0
index4 = 4
#swap
deployment_targets[index1] , deployment_targets[index4]= deployment_targets[index4] ,deployment_targets[index1]
#list_change = deployment_targets[4]
#list_change2 = deployment_targets[0]
#deployment_targets[0] =list_change[0]
#deployment_targets[4]= list_change2[0]
print(deployment_targets)

print(deployment_targets[-2])

deployment_targets[0]= "coco"
#len = deployment_targets.len()
print(len(deployment_targets))

print(deployment_targets)

deployment_targets.append("mama")
deployment_targets[1] = "yoni"
print(deployment_targets)