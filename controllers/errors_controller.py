from fastapi import HTTPException, status

wrong_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials"
)

wrong_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong token"
)

user_not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Client not found"
)

wrong_password_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong password"
)

passwords_match_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Passwords do not match"
)

user_not_create_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not create client"
)

user_exists_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Client with this email already exists",
)

meeting_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create meeting"
)

meeting_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="This meeting already exists"
)


interest_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create interest"
)

client_connect_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="The user is already present in this meeting",
)

connect_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="This connect already exists"
)

no_meeting_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong meeting id"
)

connect_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Could not create connect to meeting",
)

meeting_failed_update = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to change the meeting"
)

purchase_failed_create = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create purchase"
)

purchase_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="This purchase already exists"
)

comment_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create comment"
)


comment_not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Comment not found"
)

comment_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="This comment already exists"
)
