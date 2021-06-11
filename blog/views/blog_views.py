from flask import Blueprint, render_template

from blog.models import Post

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/list/')
def _list():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('blog.html', post_list = post_list)

@bp.route('/detail/<int:postID>/')
def detail(postID):
    post = Post.query.get_or_404(postID)
    return render_template('post_detail.html', post=post)