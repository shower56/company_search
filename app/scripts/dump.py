import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import DATABASE_URL
from models.company import CompanyName, Company, CompanyTag, Tag, TagName

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()


def run():

    f = open('company_tag_sample.csv', 'r', encoding='utf-8')
    reader = csv.reader(f)

    for line in reader:
        company_names = {
            "ko": line["company_ko"],
            "en": line["company_en"],
            "jp": line["company_ja"],
        }
        company_names = []
        company = Company()
        for lang, name in company_names.items():
            if name:
                company_name = CompanyName(company_id=company.id, language_code=lang, name=name)
                company_names.append(company_name)
        db.add_all(company_names)

        ko_tags = str(line["tag_ko"]).split("|")
        en_tags = str(line["tag_en"]).split("|")
        jp_tags = str(line["tag_ja"]).split("|")

        for ko, en, jp in zip(ko_tags, en_tags, jp_tags):
            tag_names = {"ko": ko.strip(), "en": en.strip(), "jp": jp.strip()}

            tag = Tag()
            db.add(tag)
            db.flush()
            tag_names_list = []
            for lang, name in tag_names.items():
                if name:
                    tag_name = TagName(tag_id=tag.id, language_code=lang, name=name)
                    tag_names_list.append(tag_name)

            db.add_all(tag_names_list)
            company_tag = CompanyTag(company_id=company.id, tag_id=tag.id)
            db.add(company_tag)
        db.flush()
    db.commit()


if __name__ == "__main__":
    run()
