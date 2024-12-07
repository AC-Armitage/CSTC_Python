def getPublicIP():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to get public IP"
    except Exception as e:
        return f"Error: {e}"
