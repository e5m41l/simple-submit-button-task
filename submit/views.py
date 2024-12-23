import requests
from django.shortcuts import render
from django.http import HttpResponse


CLOUD_SERVICE_URL = 'https://abc-xyz123-service-endpoint.com/submit'

def submit_view(request):
    if request.method == 'POST':
        #data = {'status': 'submitted'}
        try:
            # Calling the method that sends the POST request
            # response_data, error = send_post_request(CLOUD_SERVICE_URL, data)

            """
                I will provide my own response data and error variables 
                as I don't have access to a cloud service so, I will not call the method
            """
            response_data, error = { 'data' : 'Bow!' }, None
            if error:
                # If there was an error during the POST request we display the error message
                return render(request, 'submit/failure.html')
            
            # If the POST request was successful we return the response from the cloud service
            return render(request, 'submit/thank_you.html', response_data)

        except Exception as e:
            # Catch any unexpected errors that might occur
            return HttpResponse(f"An unexpected error occurred: {str(e)}")
        
    return render(request, 'submit/submit_form.html')



def send_post_request(API_GATEWAY_URL, data):
    """
    This method sends the POST request to the cloud service endpoint
    and returns the response.
    """
    try:
        # Send the POST request to the API Gateway
        response = requests.post(API_GATEWAY_URL, json=data)
        response.raise_for_status()  # Raises errors for bad responses (4xx, 5xx)

        # Return the response data
        return response.json(), None  # return None -> no error

    except requests.exceptions.RequestException as e:
        return None, str(e) # Handle any exception and return the error message