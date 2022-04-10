class CreatePosts < ActiveRecord::Migration[6.1]
  def change
    create_table :posts do |t|
      t.string :text
      t.string :keyword#pode sair

      t.references :user, null:false, foreign_key:true

      t.timestamps
    end
  end
end
