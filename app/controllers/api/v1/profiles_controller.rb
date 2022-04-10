module Api
  module V1
    class ProfilesController < ApplicationController
      # GET /profiles or /profiles.json
      def index
        profiles = Profile.order(:created_at)
        render json: {status: 'SUCCESS', message: 'Profile loaded', data: profiles}, status: :ok
      end

      # GET /profiles/1 or /profiles/1.json
      def show
        profile = Profile.find(params[:id])
        render json: {status: 'SUCCESS', message:'Profile loaded', data: profile}, status: :ok
      end

      # GET /profiles/new
      # def new
      #   @profile = Profile.new
      # end

      # GET /profiles/1/edit
      # def edit
      # end

      # POST /profiles or /profiles.json
      def create
        profile = Profile.new(profile_params)

        if profile.save
          render json: {status: 'SUCCESS', message: 'profile created successfully', data:profile}, status: :ok
        else
          render json: {status: 'ERROR', message: 'profile does not created', data:profile.errors}, status: :unprocessable_entity
        end  
      end

      # PATCH/PUT /profiles/1 or /profiles/1.json
      def update
        profile = Profile.find(params[:id])

        if profile.update(profile_params)
            render json: {status: 'SUCCESS', message:'Profile updated', data: profile},status: :ok
        else
            render json: {status: 'ERROR', message: 'Profile does not updated', data: profile.errors},status: :unprocessable_entity
        end
      end

      # DELETE /profiles/1 or /profiles/1.json
      def destroy
        profile = Profile.find(params[:id])
        profile.destroy
        render json: {status: 'SUCCESS', message: 'Profile deleted', data: profile}, status: :ok
      end

      private
        # Use callbacks to share common setup or constraints between actions.
        # def set_profile
        #   @profile = Profile.find(params[:id])
        # end

        # Only allow a list of trusted parameters through.
        def profile_params
          params.require(:profile).permit(:team, :interest, :user_id)
        end
    end
  end
end

