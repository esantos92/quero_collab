module Api
  module V1
    class PostsController < ApplicationController
      # GET /posts or /posts.json
      def index
        posts = Post.order(:created_at)
        render json: {status: 'SUCCESS', message:'Posts loaded', data: posts}, status: :ok 
      end

      # GET /posts/1 or /posts/1.json
      def show
        post = Post.find(params[:id])
        render json: {status: 'SUCCESS', message:'Post loaded', data: post}, status: :ok
      end

      # POST /posts or /posts.json
      def create
        post = Post.new(post_params)

        if post.save
          render json: {status: 'SUCCESS', message: 'post created successfully', data:post}, status: :ok
        else
          render json: {status: 'ERROR', message: 'post does not created', data:post.errors}, status: :unprocessable_entity
        end        
      end

      # PATCH/PUT /posts/1 or /posts/1.json
      def update
        post = Post.find(params[:id])

        if post.update(post_params)
            render json: {status: 'SUCCESS', message:'Post updated', data: post},status: :ok
        else
            render json: {status: 'ERROR', message: 'Post does not updated', data: post.errors},status: :unprocessable_entity
        end
      end

      # DELETE /posts/1 or /posts/1.json
      def destroy
        post = Post.find(params[:id])
        post.destroy
        render json: {status: 'SUCCESS', message: 'Post deleted', data: post}, status: :ok
      end

      private
      
        def post_params
          params.require(:post).permit(:text, :user_id)
        end
    end
  end
end
