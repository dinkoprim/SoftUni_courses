from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    VALID_INFLUENCER_TYPES = ["PremiumInfluencer", "StandardInfluencer"]
    VALID_CAMPAIGN_TYPES = ["HighBudgetCampaign", "LowBudgetCampaign"]
    INFLUENCER_CLASSES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }
    CAMPAIGN_CLASSES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        influencer_class = self.INFLUENCER_CLASSES[influencer_type]
        influencer = influencer_class(username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        campaign_class = self.CAMPAIGN_CLASSES[campaign_type]
        campaign = campaign_class(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.get_influencer_by_username(influencer_username)
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        campaign = self.get_campaign_by_id(campaign_id)
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

        return None  # No payment, do nothing

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            total_campaign_followers = sum(influencer.reached_followers(campaign.CAMPAIGN_TYPE) for influencer in campaign.approved_influencers)

            if total_campaign_followers > 0:
                total_reached_followers[campaign] = total_campaign_followers
        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = self.get_influencer_by_username(username)
        if not influencer:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        campaign_stats = []

        for campaign in sorted_campaigns:
            brand = campaign.brand
            total_influencers = len(campaign.approved_influencers)
            total_budget = campaign.budget if campaign.budget > 0 else 0
            total_reached_followers = sum(influencer.reached_followers(campaign.CAMPAIGN_TYPE) for influencer in campaign.approved_influencers)
            total_budget_str = f"${total_budget:.2f}"
            campaign_stats.append(
                f"  * Brand: {brand}, Total influencers: {total_influencers}, Total budget: {total_budget_str}, Total reached followers: {total_reached_followers}")

        return "$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)

    def get_influencer_by_username(self, influencer_username: str):
        return next((influencer for influencer in self.influencers if influencer.username == influencer_username), None)

    def get_campaign_by_id(self, campaign_id: int):
        return next((campaign for campaign in self.campaigns if campaign.campaign_id == campaign_id), None)
