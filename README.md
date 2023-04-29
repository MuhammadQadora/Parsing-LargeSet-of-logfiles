1.Input:
    1.A dimension file DimCampaign_Daily_FULL_2017 lists campaigns.
    
    2.Three types of activity files:
    
        1.UserCenterNewsletterClicksActivity_Daily_DELTA_YYYYMMDD
        2.UserMediaAllActivity_Daily_DELTA_YYYYMMDD
        3.UserTrafficCenterActivity_Daily_DELTA_YYYYMMDD
        
2.In the dimension file, you will find a list of campaigns. Some are active and some are inactive. The active state is indicated by the column “isActiveFlag”.

3.Each campaign has an ID (“CampaignID”) that correlates to the different activity files (different columns in each file type).

4.Expected output:

    1.Per active campaign, a separate folder with 3 files:
        1.UserCenterNewsletterClicksActivity.txt.gz
        2.UserMediaAllActivity.txt.gz 
        3.UserTrafficCenterActivity.txt.gz
        
    2.Each activity file should include a header and the relevant records for that campaign.
