class CreatePosts < ActiveRecord::Migration[6.1]
  def change
    create_table :posts do |t|
      t.string :text
      t.string :keyword

      t.timestamps
    end
  end
end
