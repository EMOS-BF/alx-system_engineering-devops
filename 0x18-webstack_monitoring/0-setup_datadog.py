#!/bin/bash
import requests

def validate_server_visibility(api_key, app_key, hostname):
    url = f"https://api.datadoghq.com/api/v1/hosts"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }
    params = {
        "host_name": hostname
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["total_returned"] > 0:
                return True
        return False
    except requests.exceptions.RequestException:
        return False
