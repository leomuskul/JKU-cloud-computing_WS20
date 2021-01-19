from gmail.gmail import gmail_auth, ListThreadsMatchingQuery

service = gmail_auth()
threads = ListThreadsMatchingQuery(service, query=query)

def ListThreadsMatchingQuery(service, user_id='me', query=''):
  """List all Threads of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
           Eg.- 'label:UNREAD' for unread messages only.

  Returns:
    List of threads that match the criteria of the query. Note that the returned
    list contains Thread IDs, you must use get with the appropriate
    ID to get the details for a Thread.
  """
  try:
    response = service.users().threads().list(userId=user_id, q=query).execute()
    threads = []
    if 'threads' in response:
      threads.extend(response['threads'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().threads().list(userId=user_id, q=query,
                                        pageToken=page_token).execute()
      threads.extend(response['threads'])

    return threads
  except errors.HttpError as error:
    raise error