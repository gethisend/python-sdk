from typing import TypedDict, List, Optional, Union

class EmailAddress(TypedDict):
    name: str
    email: str

class EmailAttachment(TypedDict, total=False):
    filename: str
    s3_key: str
    download_url: str
    content_type: str
    size: int

class Email(TypedDict, total=False):
    id: int
    project_id: int
    message_id: str
    # fields that are returned by the API
    sender_details: EmailAddress
    to_details: List[EmailAddress]
    cc: List[EmailAddress]
    bcc: List[EmailAddress]
    attachments: List[EmailAttachment]
    subject: str
    content: str
    html_body: str
    text_body: str
    status: str
    direction: str
    thread_id: Optional[int]
    in_reply_to: Optional[str]
    references: Optional[str]
    created_at: str

class Thread(TypedDict):
    id: int
    project_id: int
    subject: str
    message_count: int
    latest_snippet: str
    last_message_at: str

class DNSRecord(TypedDict):
    name: str
    type: str
    value: str

class Domain(TypedDict, total=False):
    id: int
    project_id: int
    name: str
    verification_status: str
    dkim_records: str
    dns_records: List[DNSRecord]
    created_at: str
    updated_at: str

class Endpoint(TypedDict, total=False):
    id: int
    project_id: int
    name: str
    type: str
    url: str
    email: str
    email_list: List[str]
    trigger_count: int
    last_triggered_at: str
    created_at: str
    updated_at: str

class Routing(TypedDict, total=False):
    id: int
    domain_id: int
    type: str
    email_address: str
    created_at: str
    updated_at: str
    endpoints: List[Endpoint]

# Request Types
class AddDomainRequest(TypedDict):
    name: str

class AttachmentReq(TypedDict):
    filename: str
    content: str
    content_type: str

class SendEmailRequest(TypedDict, total=False):
    from_: str  # use 'from_' internally but map to 'from' when sending JSON
    to: Union[str, List[str]]
    cc: List[str]
    bcc: List[str]
    subject: str
    html: str
    text: str
    attachments: List[AttachmentReq]
    in_reply_to: str

class CreateRoutingRequest(TypedDict, total=False):
    type: str
    email_address: str
    endpoint_ids: List[int]

class UpdateRoutingRequest(TypedDict, total=False):
    email_address: str
    endpoint_ids: List[int]
