from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False, default='default')
    message_type = db.Column(db.String(20), nullable=False)  # 'user' or 'assistant'
    content = db.Column(db.Text, nullable=False)
    formatted_content = db.Column(db.Text)
    has_attachments = db.Column(db.Boolean, default=False)
    openai_thread_id = db.Column(db.String(100))
    openai_message_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    response_time_ms = db.Column(db.Integer)

    # Relationship to attachments
    attachments = db.relationship('MessageAttachment', backref='message', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'message_type': self.message_type,
            'content': self.content,
            'formatted_content': self.formatted_content,
            'has_attachments': self.has_attachments,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'attachments': [att.to_dict() for att in self.attachments]
        }

class MessageAttachment(db.Model):
    __tablename__ = 'message_attachments'

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('chat_messages.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    mime_type = db.Column(db.String(100))
    thumbnail_path = db.Column(db.String(500))
    is_processed = db.Column(db.Boolean, default=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'thumbnail_path': self.thumbnail_path,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None
        }

    @property
    def file_url(self):
        return f'/uploads/{self.filename}'

    @property
    def thumbnail_url(self):
        return f'/uploads/thumbnails/{self.thumbnail_path}' if self.thumbnail_path else None

    def delete_files(self):
        """Delete the actual files from filesystem"""
        try:
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
            if self.thumbnail_path and os.path.exists(self.thumbnail_path):
                os.remove(self.thumbnail_path)
        except Exception as e:
            print(f"Error deleting files: {e}")