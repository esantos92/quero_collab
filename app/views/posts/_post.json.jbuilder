json.extract! post, :id, :text, :keyword, :created_at, :updated_at
json.url post_url(post, format: :json)
