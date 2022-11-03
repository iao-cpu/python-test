import sys
MyApplication::MyApplication(QWidget *parent, Qt::WFlags flags)
    : QMainWindow(parent, flags)
{
    ui.setupUi(this);
 
    ui.treeWidget->setRootIsDecorated(false);
    ui.treeWidget->setIndentation(0);
 
    // First category
    {
        QTreeWidgetItem* pCategory = new QTreeWidgetItem();
        ui.treeWidget->addTopLevelItem(pCategory);
        ui.treeWidget->setItemWidget(pCategory, 0,
            new QtCategoryButton("Category 1", ui.treeWidget, pCategory));
 
        QFrame* pFrame = new QFrame(ui.treeWidget);
        QBoxLayout* pLayout = new QVBoxLayout(pFrame);
        pLayout->addWidget(new QPushButton("Btn1"));
        pLayout->addWidget(new QPushButton("Btn2"));
 
        QTreeWidgetItem* pContainer = new QTreeWidgetItem();
        pContainer->setDisabled(true);
        pCategory->addChild(pContainer);
        ui.treeWidget->setItemWidget(pContainer, 0, pFrame);
    }
 
    // Second category
    {
        QTreeWidgetItem* pCategory = new QTreeWidgetItem();
        ui.treeWidget->addTopLevelItem(pCategory);
        ui.treeWidget->setItemWidget(pCategory, 0,
            new QtCategoryButton("Category 2", ui.treeWidget, pCategory));
 
        QFrame* pFrame = new QFrame(ui.treeWidget);
        QBoxLayout* pLayout = new QHBoxLayout(pFrame);
        pLayout->addWidget(new QPushButton("Btn1"));
        pLayout->addWidget(new QPushButton("Btn2"));
 
        QTreeWidgetItem* pContainer = new QTreeWidgetItem();
        pContainer->setDisabled(true);
        pCategory->addChild(pContainer);
        ui.treeWidget->setItemWidget(pContainer, 0, pFrame);
    }
}

CategoryButton.h

class QtCategoryButton : public QPushButton
{
    Q_OBJECT
public:
    QtCategoryButton(const QString& a_Text, QTreeWidget* a_pParent,
        QTreeWidgetItem* a_pItem);
 
private slots:
    void ButtonPressed();
 
private:
    QTreeWidgetItem* m_pItem;
};

QtCategoryButton.cpp
QtCategoryButton::QtCategoryButton( const QString& a_Text,
        QTreeWidget* a_pParent, QTreeWidgetItem* a_pItem )
    : QPushButton(a_Text, a_pParent)
    , m_pItem(a_pItem)
{
    connect(this, SIGNAL(pressed()), this, SLOT(ButtonPressed()));
}
 
void QtCategoryButton::ButtonPressed()
{
    m_pItem->setExpanded( !m_pItem->isExpanded() );
}