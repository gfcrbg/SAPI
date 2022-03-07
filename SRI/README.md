# SRI --> RBG Data Migration  

Four parts to data migration:  

**1.** [Extract](https://github.com/gfcrbg/SAPI/blob/main/SRI/README.md#extract)  
**2.** [Map](https://github.com/gfcrbg/SAPI/blob/main/SRI/README.md#map)  
**3.** [Parse](https://github.com/gfcrbg/SAPI/blob/main/SRI/README.md#parse)  
**4.** [Import](https://github.com/gfcrbg/SAPI/blob/main/SRI/README.md#import)  
  
  
## Extract  
The ShopMetrics API is used to query data obtained by Strategic Reflections Inc (SRI).  

[Knowledge Base Article](https://stratreflections.shopmetrics.com/document.asp?alias=knowledgebase#/article/8af42c08-e554-4e7e-b61b-265422139dd0)  
[API](https://stratreflections.shopmetrics.com/document.asp?alias=filemanager.v2&startnodeguid={919AD2EE-B8B9-47B3-A4B6-AE3F086DDEC6})

In reference to the sheets in the [SRI -> RBG Data Transfer Template](https://docs.google.com/spreadsheets/d/1Z5bAEOPTYxf5mcP0wbOSKjydlQw6xunnAA0oo3hc0O0/edit?usp=sharing) (make a copy of this spreadsheet for your project), this is how to query and extract the relevant data:  
  
### Shops  

#### Path  
Query > ClientAnalytics > ClientAnyalytics  
  
#### Fields  

- QuerySpecification:   *copy and paste this -->* ```[Title][Loc ID][Location Address 1][Location Address 2][Location Name][Location State/Region][Location Postal Code][Date][ScorePctXX.XX][Pts][Pts Of][CustLocationProperty001][CustLocationProperty002][CustLocationProperty003][AttachmentsCount][SurveyInstances_ClientAccessStatusID][InstanceID][SurveyInstances_PrecalcRFAsOpen][SurveyInstances_PrecalcRFAsClosed][WorkflowStepID][IsBeingExported][IsExportCompletedButFailed][IsOkForExport][HoldExport][IsExportCompleted][IsSurveyInstanceViewedBySecurityUser][SurveyInstances_TimeStampLastValidated][IsSectionLevel1WeightDefinedPrecalc][Location City][SurveyInstances_RFAStatusID][ClientAuditMode][Location Photo URL][Login][Shopper Name][ORDERBY:Date|DESC]```  
  
- ClientOrFormIDs: *enter client or form ID*  
  
- *(Optional)* DateFrom:  *enter shop date  YYYY-MM-DD*  

- *(Optional)* DateTo:  *enter shop date  YYYY-MM-DD*
      
 ### Comments  
 
 #### Path  
 Query > Operations > SurveyInstanceData > Rowset 1
 
 #### Fields  
  
- ClientOrFormIDs: *enter client or form ID*  
  
- *(Optional)* DateFrom:  *enter shop date  YYYY-MM-DD*  

- *(Optional)* DateTo:  *enter shop date  YYYY-MM-DD*
  
 ### Answers  
 
 #### Path  
 Query > Operations > SurveyInstanceData > Rowset 2
 
 #### Fields  
  
- ClientOrFormIDs: *enter client or form ID*  
  
- *(Optional)* DateFrom:  *enter shop date  YYYY-MM-DD*  

- *(Optional)* DateTo:  *enter shop date  YYYY-MM-DD*
  
 ### Parser  
 
 #### Path  
 Query > Projects > FormElements 
 
 #### Fields  
  
- *(Optional)* ClientIDs: *enter client ID*  

- FormIDs: *enter form ID*  
  
- *(Optional)* DateFrom:  *enter shop date  YYYY-MM-DD*  

- *(Optional)* DateTo:  *enter shop date  YYYY-MM-DD*


## Map  
Use the [SRI -> RBG Data Transfer Template](https://docs.google.com/spreadsheets/d/1Z5bAEOPTYxf5mcP0wbOSKjydlQw6xunnAA0oo3hc0O0/edit?usp=sharing) to map and parse. 


## Parse  
Use the [SRI -> RBG Data Transfer Template](https://docs.google.com/spreadsheets/d/1Z5bAEOPTYxf5mcP0wbOSKjydlQw6xunnAA0oo3hc0O0/edit?usp=sharing) to map and parse. 


## Import  
Make a copy of the [Job Import - Template.ipynb](https://colab.research.google.com/drive/1Ww-IciRlXQ_JN-719MvRWASAWfZRhNk6#scrollTo=4P0HExNGddjx) to use for the data transfer.
