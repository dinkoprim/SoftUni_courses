from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):

    IFLUENCER_TYPE = 'StandardInfluencer'
    INITIAL_PAYMENT_PERCENTAGE = 0.45
    CAMPAIGN_MULTIPLIERS = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9
    }

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str) -> int:
        multiplier = self.CAMPAIGN_MULTIPLIERS.get(campaign_type)
        reached_followers = int((self.followers * self.engagement_rate) * multiplier)
        return reached_followers

