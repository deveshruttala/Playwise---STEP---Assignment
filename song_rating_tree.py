class RatingNode:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.left = None
        self.right = None

class SongRatingTree:
    def __init__(self):
        self.root = None

    def insert(self, name, rating):
        def _insert(node, name, rating):
            if not node:
                return RatingNode(name, rating)
            if rating < node.rating:
                node.left = _insert(node.left, name, rating)
            else:
                node.right = _insert(node.right, name, rating)
            return node

        self.root = _insert(self.root, name, rating)

    def search_by_rating(self, rating):
        def _search(node):
            if not node:
                return
            if node.rating == rating:
                print(f"{node.name} ({node.rating}★)")
            _search(node.left)
            _search(node.right)

        print(f"Songs with {rating}★:")
        _search(self.root)
