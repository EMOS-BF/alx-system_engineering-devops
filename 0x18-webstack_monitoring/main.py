#!/bin/bash
api_key = "51d8ea8ea83db3f77fc88a26632f6517"
app_key = "e073fa910c37ec45dc08c16a8620e81719efd855"
hostname = "XX-web-01"

visibility = validate_server_visibility(api_key, app_key, hostname)
if visibility:
    print("Server is visible in Datadog.")
else:
    print("Server is not visible in Datadog.")
