from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    CAMPAIGN_TYPE = 'LowBudgetCampaign'
    BUDGET = 2_500.0
    ELIGIBILITY_FACTOR = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        necessary_engagement = self.ELIGIBILITY_FACTOR * self.required_engagement
        return True if engagement_rate >= necessary_engagement else False
