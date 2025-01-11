from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_DadJIVOGbYuMq3jOuYbxBIbEETNGKi262g9R")

limit = 2
input_insta_post = 'https://www.instagram.com/p/DEjGDE2y63Z/'
def get_comments(input_insta_post,client=client,limit = limit):
    # Prepare the Actor input
    run_input = {
        "directUrls": [
            input_insta_post,
            
        ],
        "resultsLimit": limit,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("SbK00X0JYCPblD2wp").call(run_input=run_input)


    dataset_client = client.dataset(run['defaultDatasetId'])
    data_items = dataset_client.list_items().items
    df = pd.DataFrame(data_items)
    data = df[['ownerUsername','text']]
    toxic = list(data['ownerUsername'])
    # print(toxic)
    return data
# if __name__ == '__main__':
#     get_comments(input_insta_post,client)
# # Fetch and print Actor results from the run's dataset (if there are any)
# # for item in client.dataset(run["defaultDatasetId"]).iterate_items():
# #     print(item)