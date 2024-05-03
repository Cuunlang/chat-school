"""empty message

Revision ID: a700c6b08a8c
Revises: 
Create Date: 2024-05-03 14:18:17.364987

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a700c6b08a8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('대시보드')
    op.drop_table('시간표')
    op.drop_table('학생')
    op.drop_table('제출물')
    op.drop_table('문제')
    op.drop_table('챗봇')
    op.drop_table('게시판')
    op.drop_table('선생_메모장')
    op.drop_table('시험')
    op.drop_table('학생_메모장')
    op.drop_table('감정')
    op.drop_table('과제')
    op.drop_table('첨부파일')
    op.drop_table('선생')
    op.drop_table('채팅')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('채팅',
    sa.Column('채팅_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('학생_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('시간', mysql.DATETIME(), nullable=True),
    sa.Column('질문', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('챗봇응답', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['학생_ID'], ['학생.학생_ID'], name='채팅_ibfk_1'),
    sa.PrimaryKeyConstraint('채팅_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('선생',
    sa.Column('선생_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('성별', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('이름', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('생년월일', sa.DATE(), nullable=True),
    sa.Column('이메일', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('선생_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('첨부파일',
    sa.Column('파일_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('게시물_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('파일명', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('파일경로', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('시간', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['게시물_ID'], ['게시판.게시물_ID'], name='첨부파일_ibfk_1'),
    sa.PrimaryKeyConstraint('파일_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('과제',
    sa.Column('과제_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('제출자_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('대시보드', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('주차', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('제목', mysql.VARCHAR(length=25), nullable=True),
    sa.Column('내용', mysql.TEXT(), nullable=True),
    sa.Column('기한', sa.DATE(), nullable=True),
    sa.Column('유형', mysql.VARCHAR(length=5), nullable=True),
    sa.ForeignKeyConstraint(['대시보드'], ['대시보드.대시보드_key'], name='과제_ibfk_2'),
    sa.ForeignKeyConstraint(['제출자_id'], ['선생.선생_ID'], name='과제_ibfk_1'),
    sa.PrimaryKeyConstraint('과제_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('감정',
    sa.Column('감정_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('학생_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('감정', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('날짜', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['학생_id'], ['학생.학생_ID'], name='감정_ibfk_1'),
    sa.PrimaryKeyConstraint('감정_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('학생_메모장',
    sa.Column('메모_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('작성자_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('제목', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('내용', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('작성시간', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['작성자_id'], ['학생.학생_ID'], name='학생_메모장_ibfk_1'),
    sa.PrimaryKeyConstraint('메모_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('시험',
    sa.Column('시험_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('대시보드_key', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('시간', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['대시보드_key'], ['대시보드.대시보드_key'], name='시험_ibfk_1'),
    sa.PrimaryKeyConstraint('시험_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('선생_메모장',
    sa.Column('메모_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('작성자_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('제목', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('내용', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('작성시간', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['작성자_id'], ['선생.선생_ID'], name='선생_메모장_ibfk_1'),
    sa.PrimaryKeyConstraint('메모_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('게시판',
    sa.Column('게시물_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('대시보드_key', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('학생_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('제목', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('작성내용', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('작성시간', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['대시보드_key'], ['대시보드.대시보드_key'], name='게시판_ibfk_1'),
    sa.ForeignKeyConstraint(['학생_ID'], ['학생.학생_ID'], name='게시판_ibfk_2'),
    sa.PrimaryKeyConstraint('게시물_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('챗봇',
    sa.Column('챗봇_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('대시보드', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('주차', mysql.FLOAT(), nullable=True),
    sa.Column('추가시간', sa.DATE(), nullable=True),
    sa.Column('내용', mysql.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['대시보드'], ['대시보드.대시보드_key'], name='챗봇_ibfk_1'),
    sa.PrimaryKeyConstraint('챗봇_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('문제',
    sa.Column('문제_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('대시보드', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('시험_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('유형', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('문제질문', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('문제내용', mysql.TEXT(), nullable=True),
    sa.Column('보기1', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('보기2', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('보기3', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('보기4', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('보기5', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('정답', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('문항_UID', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('빈칸개수', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('빈칸1의정답', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('빈칸2의정답', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('빈칸3의정답', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('빈칸4의정답', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('빈칸5의정답', mysql.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['대시보드'], ['대시보드.대시보드_key'], name='문제_ibfk_1'),
    sa.ForeignKeyConstraint(['시험_id'], ['대시보드.대시보드_key'], name='문제_ibfk_2'),
    sa.PrimaryKeyConstraint('문제_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('제출물',
    sa.Column('제출_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('제출자_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('과제_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('제목', mysql.VARCHAR(length=25), nullable=True),
    sa.Column('내용', mysql.TEXT(), nullable=True),
    sa.Column('점수', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['과제_ID'], ['과제.과제_ID'], name='제출물_ibfk_2'),
    sa.ForeignKeyConstraint(['제출자_id'], ['학생.학생_ID'], name='제출물_ibfk_1'),
    sa.PrimaryKeyConstraint('제출_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('학생',
    sa.Column('학생_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('성별', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('이름', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('생년월일', sa.DATE(), nullable=True),
    sa.Column('휴대폰번호', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('학년', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('학급', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('학생_ID'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('시간표',
    sa.Column('시간표_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('대시보드_key', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('요일', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('시간', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['대시보드_key'], ['대시보드.대시보드_key'], name='시간표_ibfk_1'),
    sa.PrimaryKeyConstraint('시간표_id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('대시보드',
    sa.Column('대시보드_key', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('담당선생_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('과목명', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('학년', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('학급', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['담당선생_ID'], ['선생.선생_ID'], name='대시보드_ibfk_1'),
    sa.PrimaryKeyConstraint('대시보드_key'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
