select_all_characters = """
SELECT *
FROM charactercreator_character
"""

total_characters = """
SELECT COUNT(*)
FROM charactercreator_character
"""

total_mage_characters = """
SELECT COUNT(*)
FROM charactercreator_mage
"""

non_weapons = """
SELECT COUNT(*)
FROM armory_item
LEFT JOIN armory_weapon
		ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id is NULL
"""

character_items = """
SELECT c.character_id, COUNT(i.item_id)
FROM charactercreator_character AS c
JOIN charactercreator_character_inventory AS ci
		ON c.character_id = ci.character_id
JOIN armory_item AS i
		ON ci.item_id = i.item_id
GROUP BY c.character_id
LIMIT 20
"""

character_avg_items = """
SELECT AVG(item_count)
FROM (
SELECT c.character_id, COUNT(i.item_id) AS item_count
FROM charactercreator_character AS c
JOIN charactercreator_character_inventory AS ci
		ON c.character_id = ci.character_id
JOIN armory_item AS i
		ON ci.item_id = i.item_id
GROUP BY c.character_id
)
"""