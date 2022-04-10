class AddDetailsToProfile < ActiveRecord::Migration[6.1]
  def change
    add_reference :profiles, :user, index: true
    add_column :profiles, :team, :string
  end
end
