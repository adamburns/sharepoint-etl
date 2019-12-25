import json
import pandas as pd
from pandas.io.json import json_normalize
from extract import extract_projects, extract_tasks


def clean_data(data, params):
    data = json_normalize(data.json()['d']['results'])
    return data[params]


def clean_projects():
    PARAMS = [
        'Id',
        'BaseName',
        'Sponsor',
        'ReportStatus1',
        'SPW',
        'WFProgress',
        'DateInitialStage',
        'DateInProgressRFI',
        'DateInProgressDrafting',
        'DateSponsorReview',
        'DateFinalizeProject',
        'DateCompleted1',
        'ProjectLead.Title',
        'ReportType',
        'ProgramType',
        'LinkToOpportunity.Url',
        'First_x0020_Draft_x003f_',
        'QC',
        'Editor0',
        'DraftSentDate',
        'Final',
        'Sponsor.Label',
        'SPW.Description',
        'SPW.Url'
    ]
    return clean_data(extract_projects(), PARAMS)


def clean_tasks():
    PARAMS = [
        'FileSystemObjectType',
        'Id',
        'ServerRedirectedEmbedUri',
        'ServerRedirectedEmbedUrl',
        'ContentTypeId',
        'Title',
        'Priority',
        'Status',
        'PercentComplete',
        'AssignedToId',
        'AssignedToStringId',
        'Body',
        'StartDate',
        'DueDate',
        'Checkmark',
        'RelatedItems',
        'TaskOutcome',
        'Notes1',
        'Complete',
        'OnsiteAttendeesId',
        'OnsiteAttendeesStringId',
        'OnsiteStartDate',
        'OnsiteEndDate',
        'IsThereAnOnsite',
        'KickOffCallStartDate',
        'KickOffCallEndDate',
        'DraftSentDate',
        'Project_x0020_Name',
        'Clarity_x0020_of_x0020_Thought',
        'Readability',
        'Mechanics',
        'Consistency',
        'Report_x0020_Section_x003a__x002',
        'Report_x0020_Section_x003a__x0020',
        'Report_x0020_Section_x003a__x0021',
        'Report_x0020_Section_x003a__x0022',
        'Report_x0020_Section_x003a__x0023',
        'Report_x0020_Section_x003a__x0024',
        'Created',
        'Modified',
        'DateRetainerReceived',
        'ComplianceAssetId',
        'ID',
        'AuthorId',
        'EditorId',
        'OData__UIVersionString',
        'Attachments',
        'GUID',
        '__metadata.id',
        '__metadata.uri',
        '__metadata.etag',
        '__metadata.type',
        'FirstUniqueAncestorSecurableObject.__deferred.uri',
        'RoleAssignments.__deferred.uri',
        'AttachmentFiles.__deferred.uri',
        'ContentType.__deferred.uri',
        'GetDlpPolicyTip.__deferred.uri',
        'FieldValuesAsHtml.__deferred.uri',
        'FieldValuesAsText.__deferred.uri',
        'FieldValuesForEdit.__deferred.uri',
        'File.__deferred.uri',
        'Folder.__deferred.uri',
        'LikedByInformation.__deferred.uri',
        'ParentList.__deferred.uri',
        'Properties.__deferred.uri',
        'Versions.__deferred.uri',
        'PredecessorsId.__metadata.type',
        'PredecessorsId.results',
        'PreviouslyAssignedToStringId.__metadata.type',
        'PreviouslyAssignedToStringId.results',
        'PreviouslyAssignedToStringId'
    ]
    return clean_data(extract_tasks(), PARAMS)
