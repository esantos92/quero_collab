module Api
  module V1
    class UsersController < ApplicationController
      # GET /users or /users.json
      def index
        users = User.order(:created_at)
        render json: {status: 'SUCCESS', message: 'Users loaded', data: users}, status: :ok
      end

      # GET /users/1 or /users/1.json
      def show
        user = User.find(params[:id])
        render json: {status: 'SUCCESS', message: 'User loaded', data: user}, status: :ok
      end

      # POST /users or /users.json
      def create
        user = User.new(user_params)
        
          if user.save
            render json: {status: 'SUCCESS', message: 'User created successfully', data: user}, status: :ok
          else
            render json: {status: 'ERROR', message: 'User does not created', data: user.errors}, status: :unprocessable_entity
          end
      end

      # PATCH/PUT /users/1 or /users/1.json
      def update
        user = User.find(params[:id])

        if user.update(user_params)
          render json: {status: 'SUCCESS', message: 'User updated successfully', data: user}, status: :ok
        else
          render json: {status: 'ERROR', message: 'User does not updated', data: user.errors}, status: :unprocessable_entity
        end    
      end

      # DELETE /users/1 or /users/1.json
      def destroy
        user = User.find(params[:id])

        user.destroy
        render json: {status: 'SUCCESS', message: 'User was successfully destroyed', data: user}, status: :ok
        
      end

      private
      
        def user_params
          params.require(:user).permit(:name)
        end
    end
  end
end
