from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMediaClass(TestCase):
    username = 'test_user'
    platform = 'Instagram'
    followers = 1000
    content_type = 'photo'

    def setUp(self):
        self.social_media = SocialMedia(self.username, self.platform, self.followers, self.content_type)

    def test_social_media_structure(self):
        self.assertTrue(hasattr(SocialMedia, "create_post"))
        self.assertTrue(hasattr(SocialMedia, "like_post"))
        self.assertTrue(hasattr(SocialMedia, "comment_on_post"))

        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))

    def test_init(self):
        self.assertEqual(self.social_media._username, self.username)
        self.assertEqual(self.social_media._platform, self.platform)
        self.assertEqual(self.social_media._followers, self.followers)
        self.assertEqual(self.social_media._content_type, self.content_type)
        self.assertEqual(self.social_media._posts, [])

    def test_platform_with_invalid_value__expect_to_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media = SocialMedia(self.username, 'InvalidPlatform', self.followers, self.content_type)

        expected_error_message = "Platform should be one of ['Instagram', 'YouTube', 'Twitter']"
        actual_error_message = str(ve.exception)
        self.assertEqual(expected_error_message, actual_error_message)

    def test_followers_with_negative_value__expect_to_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -100

        expected_error_message = "Followers cannot be negative."
        actual_error_message = str(ve.exception)
        self.assertEqual(expected_error_message, actual_error_message)

    def test_create_post_success(self):
        post_content = "This is a test post."
        expected_output = f"New {self.content_type} post created by {self.username} on {self.platform}."
        actual_output = self.social_media.create_post(post_content)
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(len(self.social_media._posts), 1)

    def test_like_post_success(self):
        post_content = "This is a test post."
        self.social_media.create_post(post_content)
        expected_output = f"Post liked by {self.username}."
        actual_output = self.social_media.like_post(0)
        self.assertEqual(expected_output, actual_output)

    def test_like_post_max_likes_reached(self):
        post_content = "This is a test post."
        self.social_media.create_post(post_content)
        # Liking the post 10 times
        for _ in range(10):
            self.social_media.like_post(0)
        expected_output = "Post has reached the maximum number of likes."
        actual_output = self.social_media.like_post(0)
        self.assertEqual(expected_output, actual_output)

    def test_comment_on_post_success(self):
        post_content = "This is a test post."
        self.social_media.create_post(post_content)
        comment = "Great post!"
        expected_output = f"Comment added by {self.username} on the post."
        actual_output = self.social_media.comment_on_post(0, comment)
        self.assertEqual(expected_output, actual_output)

    def test_comment_on_post_invalid_comment_length(self):
        post_content = "This is a test post."
        self.social_media.create_post(post_content)
        comment = "Short"
        expected_output = "Comment should be more than 10 characters."
        actual_output = self.social_media.comment_on_post(0, comment)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    main()