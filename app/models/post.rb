class Post < ApplicationRecord
  belongs_to :user

  validates :text , presence: true, length: {maximum: 1000,
    too_long: "%{count} characters is the maximun allowed"}

  validates :user_id, presence: true
end
